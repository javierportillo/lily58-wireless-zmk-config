/* SPDX-License-Identifier: MIT */

#include <zephyr/device.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/drivers/uart/cdc_acm.h>
#include <zephyr/init.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/reboot.h>

#include <dt-bindings/zmk/reset.h>
#include <zmk/usb.h>

static const struct device *const usb_uart = DEVICE_DT_GET(DT_CHOSEN(zmk_studio_rpc_uart));

static void check_closed_port(struct k_work *work);
static K_WORK_DELAYABLE_DEFINE(bootloader_check, check_closed_port);

static void check_closed_port(struct k_work *work) {
    ARG_UNUSED(work);
    uint32_t baud, dtr;

    /* Do not enter the bootloader merely because USB was unplugged. */
    if (!zmk_usb_is_hid_ready() ||
        uart_line_ctrl_get(usb_uart, UART_LINE_CTRL_BAUD_RATE, &baud) < 0 || baud != 1200 ||
        uart_line_ctrl_get(usb_uart, UART_LINE_CTRL_DTR, &dtr) < 0) {
        return;
    }

    if (!dtr) {
        /* ZMK v0.3's nRF52 reboot hook stores this type in GPREGRET. */
        sys_reboot(RST_UF2);
        return;
    }

    /* Only a port held open at 1200 baud needs further checks. */
    k_work_reschedule(&bootloader_check, K_MSEC(100));
}

static void baud_changed(const struct device *dev, uint32_t baud) {
    ARG_UNUSED(dev);
    if (baud == 1200) {
        /* Run outside the USB callback and allow the host to close the port. */
        k_work_reschedule(&bootloader_check, K_MSEC(250));
    } else {
        k_work_cancel_delayable(&bootloader_check);
    }
}

static int usb_bootloader_init(void) {
    if (!device_is_ready(usb_uart)) {
        return -ENODEV;
    }
    return cdc_acm_dte_rate_callback_set(usb_uart, baud_changed);
}

SYS_INIT(usb_bootloader_init, APPLICATION, CONFIG_APPLICATION_INIT_PRIORITY);
