/*
Copyright 2019 @foostan
Copyright 2020 Drashna Jaelre <@drashna>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include QMK_KEYBOARD_H
#include "raw_hid.h"

enum custom_keycodes
{
    M_curly_brackets = SAFE_RANGE,
    M_square_brackets,
    M_round_brackets,
    M_angle_brackets,
    M_arrow_left,
    M_arrow_right,

};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT_split_3x6_3(KC_TAB, KC_Q, KC_W, KC_E, KC_R, KC_T, KC_Y, KC_U, KC_I, KC_O, KC_P, KC_ESC, KC_BSPC, KC_A, KC_S, KC_D, KC_F, KC_G, KC_H, KC_J, KC_K, KC_L, KC_TRNS, KC_QUOT, KC_LALT, KC_Z, KC_X, KC_C, KC_V, KC_B, KC_N, KC_M, KC_COMM, KC_DOT, KC_EQL, KC_LGUI, KC_LCTL, KC_SPC, OSL(4), OSL(5), KC_ENT, KC_LSFT),
    [1] = LAYOUT_split_3x6_3(KC_TAB, KC_Q, KC_W, KC_E, KC_R, KC_T, KC_Y, KC_U, KC_I, KC_O, KC_P, KC_ESC, KC_BSPC, KC_A, KC_S, KC_D, KC_F, KC_G, KC_H, KC_J, KC_K, KC_L, LSFT(KC_SCLN), KC_QUOT, OSM(MOD_LALT), KC_Z, KC_X, KC_C, KC_V, KC_B, KC_N, KC_M, KC_COMM, KC_DOT, KC_EQL, KC_LGUI, OSM(MOD_LCTL), LT(2, KC_SPC), OSL(4), OSL(5), LT(3, KC_ENT), KC_TRNS),
    [2] = LAYOUT_split_3x6_3(LALT(KC_TAB), KC_LALT, LCTL(KC_LEFT), KC_UP, LCTL(KC_RGHT), KC_PGUP, KC_NO, KC_LCBR, KC_LBRC, KC_LPRN, KC_LT, KC_TRNS, KC_DEL, LT(5, KC_ENT), KC_LEFT, KC_DOWN, KC_RGHT, LCTL(KC_RBRC), KC_MUTE, KC_BTN1, KC_BTN3, KC_BTN2, KC_SCLN, KC_GRV, KC_LSFT, LCTL(LSFT(KC_Z)), KC_HOME, LALT(LSFT(KC_F6)), KC_END, KC_PGDN, KC_NO, KC_EXLM, KC_VOLD, KC_VOLU, KC_QUES, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, LSFT(KC_ENT), KC_TRNS),
    [3] = LAYOUT_split_3x6_3(KC_TRNS, KC_PLUS, KC_MINS, KC_ASTR, KC_PERC, KC_AMPR, KC_PIPE, KC_RCBR, KC_RBRC, KC_RPRN, KC_GT, KC_TRNS, KC_TRNS, KC_1, KC_2, KC_3, KC_4, KC_5, KC_6, KC_7, KC_8, KC_9, KC_0, KC_DQUO, KC_TRNS, KC_AT, KC_UNDS, KC_HASH, KC_TILD, KC_CIRC, KC_DLR, KC_BSLS, KC_COMM, KC_DOT, KC_SLSH, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS),
    [4] = LAYOUT_split_3x6_3(LALT(LSFT(KC_F7)), KC_F11, KC_F12, LALT(LSFT(KC_F3)), LALT(LSFT(KC_F4)), LALT(LSFT(KC_F5)), KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_TRNS, LALT(LSFT(KC_F8)), KC_F1, KC_F2, KC_F3, KC_F4, KC_F5, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_TRNS, KC_F6, KC_F7, KC_F8, KC_F9, KC_F10, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_TRNS, KC_TRNS, OSL(3), TO(1), KC_TRNS, KC_TRNS, KC_TRNS),
    [5] = LAYOUT_split_3x6_3(KC_TRNS, KC_NO, KC_7, KC_8, KC_9, KC_0, KC_NO, M_curly_brackets, M_square_brackets, M_round_brackets, M_angle_brackets, KC_TRNS, KC_NO, KC_NO, KC_4, KC_5, KC_6, LCTL(KC_LBRC), KC_NO, KC_NO, KC_NO, KC_NO, MO(6), KC_NO, KC_TRNS, KC_NO, KC_1, KC_2, KC_3, KC_DOT, KC_NO, KC_NO, M_arrow_left, M_arrow_right, KC_NO, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, TO(1), TO(0), KC_NO),
    [6] = LAYOUT_split_3x6_3(KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, RGB_HUD, RGB_VAI, RGB_HUI, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, RGB_TOG, RGB_SAD, RGB_VAD, RGB_SAI, KC_TRNS, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO)};

void keyboard_post_init_user(void)

{
    // Customise these values to desired behaviour
    // debug_enable = true;
    // debug_matrix = true;
    // debug_keyboard=true;
    // debug_mouse=true;
    layer_move(1);
};

#ifdef RAW_ENABLE
#ifdef VIAL_ENABLE
void raw_hid_receive_kb(uint8_t *data, uint8_t length)
{
    if (data[1] == 1)
    {
        // default_layer_set(data[1]);
        layer_move(data[2]);
    }
    raw_hid_send(data, length);
}
#else
void raw_hid_receive(uint8_t *data, uint8_t length)
{
    if (data[0] == 1)
    {
        // default_layer_set(data[1]);
        layer_move(data[1]);
    }
    raw_hid_send(data, length);
}
#endif
#endif

#ifdef OLED_ENABLE
#include <stdio.h>

oled_rotation_t oled_init_user(oled_rotation_t rotation)
{
    if (!is_keyboard_master())
    {
        return OLED_ROTATION_180; // flips the display 180 degrees if offhand
    }
    return rotation;
}

#define L_BASE 0
#define L_LOWER 2
#define L_RAISE 4
#define L_ADJUST 8
enum layer_number
{
    L_N_0 = 0,
    L_N_1 = 1,
    L_N_2 = 2,
    L_N_3 = 3,
    L_N_4 = 4,
    L_N_5 = 5,
    L_N_6 = 6,
    L_N_7 = 7,
    L_N_8 = 8,
    L_N_9 = 9,
    L_N_10 = 10,
};
void oled_render_layer_state(void)
{
    oled_write_P(PSTR("Layer: "), false);

    switch (get_highest_layer(layer_state))
    {
    case L_N_0:
        oled_write_ln_P(PSTR("0_game"), false);
        break;
    case L_N_1:
        oled_write_ln_P(PSTR("1_qwert"), false);
        break;
    case L_N_2:
        oled_write_ln_P(PSTR("2_cursor"), false);
        break;
    case L_N_3:
        oled_write_ln_P(PSTR("3_symbol"), false);
        break;
    case L_N_4:
        oled_write_ln_P(PSTR("4_fn"), false);
        break;
    case L_N_5:
        oled_write_ln_P(PSTR("5_pad_str"), false);
        break;
    case L_N_6:
        oled_write_ln_P(PSTR("6_rgb"), false);
        break;
    case L_N_7:
        oled_write_ln_P(PSTR("7"), false);
        break;
    case L_N_8:
        oled_write_ln_P(PSTR("8"), false);
        break;
    default:
        oled_write_ln_P(PSTR("Undefined"), false);
    }
}

char keylog_str[24] = {};

const char code_to_name[60] = {' ', ' ', ' ', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'R', 'E', 'B', 'T', '_', '-', '=', '[', ']', '\\', '#', ';', '\'', '`', ',', '.', '/', ' ', ' ', ' '};

void set_keylog(uint16_t keycode, keyrecord_t *record)
{
    char name = ' ';
    if ((keycode >= QK_MOD_TAP && keycode <= QK_MOD_TAP_MAX) || (keycode >= QK_LAYER_TAP && keycode <= QK_LAYER_TAP_MAX))
    {
        keycode = keycode & 0xFF;
    }
    if (keycode < 60)
    {
        name = code_to_name[keycode];
    }

    // update keylog
    snprintf(keylog_str, sizeof(keylog_str), "%dx%d, k%2d, %c", record->event.key.row, record->event.key.col, keycode, name);
}

void oled_render_keylog(void)
{
    oled_write(keylog_str, false);
}

void render_bootmagic_status(bool status)
{
    /* Show Ctrl-Gui Swap options */
    static const char PROGMEM logo[][2][3] = {
        {{0x97, 0x98, 0}, {0xb7, 0xb8, 0}},
        {{0x95, 0x96, 0}, {0xb5, 0xb6, 0}},
    };
    if (status)
    {
        oled_write_ln_P(logo[0][0], false);
        oled_write_ln_P(logo[0][1], false);
    }
    else
    {
        oled_write_ln_P(logo[1][0], false);
        oled_write_ln_P(logo[1][1], false);
    }
}

void oled_render_logo(void)
{
    static const char PROGMEM crkbd_logo[] = {0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8a, 0x8b, 0x8c, 0x8d, 0x8e, 0x8f, 0x90, 0x91, 0x92, 0x93, 0x94, 0xa0, 0xa1, 0xa2, 0xa3, 0xa4, 0xa5, 0xa6, 0xa7, 0xa8, 0xa9, 0xaa, 0xab, 0xac, 0xad, 0xae, 0xaf, 0xb0, 0xb1, 0xb2, 0xb3, 0xb4, 0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xca, 0xcb, 0xcc, 0xcd, 0xce, 0xcf, 0xd0, 0xd1, 0xd2, 0xd3, 0xd4, 0};
    oled_write_P(crkbd_logo, false);
}

bool oled_task_user(void)
{
    if (is_keyboard_master())
    {
        oled_render_layer_state();
        oled_render_keylog();
    }
    else
    {
        oled_render_logo();
    }
    return false;
}

#endif // OLED_ENABLE

bool process_record_user(uint16_t keycode, keyrecord_t *record)
{
    if (record->event.pressed)
    {
        switch (keycode)
        {
        case M_curly_brackets:
            SEND_STRING("{}" SS_TAP(X_LEFT));
            return false;
            break;
        case M_square_brackets:
            SEND_STRING("[]" SS_TAP(X_LEFT));
            return false;
            break;
        case M_round_brackets:
            SEND_STRING("()" SS_TAP(X_LEFT));
            return false;
            break;
        case M_angle_brackets:
            SEND_STRING("<>" SS_TAP(X_LEFT));
            return false;
            break;
        case M_arrow_left:
            SEND_STRING("<=");
            return false;
            break;
        case M_arrow_right:
            SEND_STRING("=>");
            return false;
            break;
        }
    }

#ifdef OLED_ENABLE
    if (record->event.pressed)
    {
        set_keylog(keycode, record);
    }
#endif
#ifdef CONSOLE_ENABLE
    // uprintf("KL: kc: 0x%04X, col: %2u, row: %2u, pressed: %u, time: %5u, int: %u, count: %u\n", keycode, record->event.key.col, record->event.key.row, record->event.pressed, record->event.time, record->tap.interrupted, record->tap.count);
#endif
    return true;
};
