# -*- coding: utf-8 -*-
from collections import deque
import logging
import locale
locale.setlocale(locale.LC_ALL, "")
logger = logging.getLogger(__name__)

import locale
locale.setlocale(locale.LC_ALL, "")


class Window_Stack_Constants(object):
    ''' Modes of Operation '''
    DEPENDENCY_ERROR = -2
    NO_PLAYER_ERROR_MODE = -1
    NORMAL_MODE = 0
    PLAYLIST_MODE = 1
    REGISTER_MODE = 2
    SEARCH_NORMAL_MODE = 3
    SEARCH_PLAYLIST_MODE = 4
    SEARCH_THEME_MODE = 5
    SEARCH_SELECT_PLAYLIST_MODE = 6
    SEARCH_SELECT_STATION_MODE = 7
    CONFIG_MODE = 8
    SELECT_PLAYER_MODE = 9
    SELECT_ENCODING_MODE = 10
    SELECT_PLAYLIST_MODE = 11
    SELECT_STATION_MODE = 12
    SELECT_STATION_ENCODING_MODE = 13
    NEW_THEME_MODE = 14
    EDIT_THEME_MODE = 15
    EDIT_STATION_ENCODING_MODE = 16
    IN_PLAYER_PARAMS_EDITOR = 17
    REMOVE_STATION_MODE = 50
    SAVE_PLAYLIST_MODE = 51
    ASK_TO_SAVE_PLAYLIST_WHEN_OPENING_PLAYLIST_MODE = 52
    ASK_TO_SAVE_PLAYLIST_WHEN_BACK_IN_HISTORY_MODE = 53
    ASK_TO_SAVE_PLAYLIST_WHEN_EXITING_MODE = 54
    ADD_STATION_MODE = 55
    EDIT_STATION_MODE = 56
    CLEAR_REGISTER_MODE = 57
    CLEAR_ALL_REGISTERS_MODE = 58
    STATION_INFO_MODE = 59
    CREATE_PLAYLIST_MODE = 60
    RENAME_PLAYLIST_MODE = 61
    COPY_PLAYLIST_MODE = 62
    CONNECTION_MODE = 63
    PASTE_MODE = 64
    UNNAMED_REGISTER_MODE = 65
    PLAYER_PARAMS_MODE = 66
    STATION_DATABASE_INFO_MODE = 67
    VOTE_RESULT_MODE = 68
    BROWSER_SORT_MODE = 69
    BROWSER_SERVER_SELECTION_MODE = 70
    BROWSER_SEARCH_MODE = 71
    BROWSER_OPEN_MODE = 72
    BROWSER_PERFORMING_SEARCH_MODE = 73
    RADIO_BROWSER_CONFIG_MODE = 74
    SCHEDULE_EDIT_MODE = 75
    REMOVE_GROUP_MODE = 76
    RECORD_WINDOW_MODE = 77
    BUFFER_SET_MODE = 78
    SCHEDULE_PLAYER_SELECT_MODE = 79
    SCHEDULE_STATION_SELECT_MODE = 80
    MAIN_HELP_MODE = 100
    MAIN_HELP_MODE_PAGE_2 = 101
    MAIN_HELP_MODE_PAGE_3 = 102
    MAIN_HELP_MODE_PAGE_4 = 103
    MAIN_HELP_MODE_PAGE_5 = 104
    PLAYLIST_HELP_MODE = 105
    CONFIG_HELP_MODE = 106
    THEME_HELP_MODE = 107
    SELECT_PLAYER_HELP_MODE = 108
    SELECT_ENCODING_HELP_MODE = 109
    SELECT_PLAYLIST_HELP_MODE = 110
    SELECT_STATION_HELP_MODE = 111
    NEW_THEME_HELP_MODE = 112
    EDIT_THEME_HELP_MODE = 113
    ASK_TO_CREATE_NEW_THEME_MODE = 114
    SEARCH_HELP_MODE = 115
    LINE_EDITOR_HELP_MODE = 116
    REGISTER_HELP_MODE = 117
    EXTRA_COMMANDS_HELP_MODE = 118
    YANK_HELP_MODE = 119
    MOUSE_RESTART_INFO_MODE = 120
    IN_PLAYER_PARAMS_EDITOR_HELP_MODE = 121
    RADIO_BROWSER_SEARCH_HELP_MODE = 122
    RADIO_BROWSER_CONFIG_HELP_MODE = 123
    ASK_TO_SAVE_BROWSER_CONFIG_FROM_BROWSER = 124
    ASK_TO_SAVE_BROWSER_CONFIG_FROM_CONFIG = 125
    ASK_TO_SAVE_BROWSER_CONFIG_TO_EXIT = 126
    WIN_MANAGE_PLAYERS_MSG_MODE = 127
    WIN_PRINT_EXE_LOCATION_MODE = 128
    WIN_UNINSTALL_MODE = 129
    WIN_REMOVE_OLD_INSTALLATION_MODE = 130
    SCHEDULE_EDIT_HELP_MODE = 131
    REMOTE_CONTROL_SERVER_ACTIVE_MODE = 132
    REMOTE_CONTROL_SERVER_NOT_ACTIVE_MODE = 133
    CHANGE_PLAYER_MODE = 134
    ASK_TO_UPDATE_STATIONS_CSV_MODE = 135
    UPDATE_STATIONS_CSV_RESULT_MODE = 136
    GROUP_SELECTION_MODE = 137
    GROUP_SEARCH_MODE = 138
    GROUP_HELP_MODE = 139
    # TODO: return values from opening theme
    PLAYLIST_RECOVERY_ERROR_MODE = 200
    PLAYLIST_NOT_FOUND_ERROR_MODE = 201
    PLAYLIST_LOAD_ERROR_MODE = 202
    PLAYLIST_RELOAD_ERROR_MODE = 203
    PLAYLIST_RELOAD_CONFIRM_MODE = 204
    PLAYLIST_DIRTY_RELOAD_CONFIRM_MODE = 205
    PLAYLIST_SCAN_ERROR_MODE = 206
    SAVE_PLAYLIST_ERROR_1_MODE = 207
    SAVE_PLAYLIST_ERROR_2_MODE = 208
    REQUESTS_MODULE_NOT_INSTALLED_ERROR = 209
    UNKNOWN_BROWSER_SERVICE_ERROR = 210
    SERVICE_CONNECTION_ERROR = 211
    PLAYER_CHANGED_INFO_MODE = 212
    DNSPYTHON_MODULE_NOT_INSTALLED_ERROR = 213
    FOREIGN_PLAYLIST_ASK_MODE = 300
    FOREIGN_PLAYLIST_MESSAGE_MODE = 301
    FOREIGN_PLAYLIST_COPY_ERROR_MODE = 302
    CONFIG_SAVE_ERROR_MODE = 303
    EDIT_STATION_NAME_ERROR = 304
    EDIT_STATION_URL_ERROR = 305
    PY2_EDITOR_ERROR = 306
    REGISTER_SAVE_ERROR_MODE = 307
    STATION_INFO_ERROR_MODE = 308
    PLAYLIST_COPY_ERROR = 309
    PLAYLIST_RENAME_ERROR = 310
    PLAYLIST_CREATE_ERROR = 311
    PLAYLIST_NOT_SAVED_ERROR_MODE = 312
    USER_PARAMETER_ERROR = 313
    BROWSER_CONFIG_SAVE_ERROR_MODE = 314
    SERVICE_SERVERS_UNREACHABLE = 315
    REMOTE_CONTROL_SERVER_START_ERROR_MODE = 316
    REMOTE_CONTROL_SERVER_DEAD_ERROR_MODE = 317
    REMOTE_CONTROL_SERVER_ERROR_MODE = 318
    NETIFACES_MODULE_NOT_INSTALLED_ERROR = 319
    CHANGE_PLAYER_ONE_PLAYER_ERROR_MODE = 320
    CHANGE_PLAYER_SAME_PLAYER_ERROR_MODE = 321
    EDIT_STATION_ICON_URL_ERROR = 322
    EDIT_STATION_ICON_FORMAT_ERROR = 323
    WIN_VLC_NO_RECORD_MODE = 324
    SCHEDULE_ERROR_MODE = 325
    THEME_MODE = 400
    HISTORY_EMPTY_NOTIFICATION = 500
    NO_BROWSER_SEARCH_RESULT_NOTIFICATION = 501
    UPDATE_NOTIFICATION_MODE = 1000
    UPDATE_NOTIFICATION_OK_MODE = 1001
    UPDATE_NOTIFICATION_NOK_MODE = 1002
    SESSION_LOCKED_MODE = 1003
    NOT_IMPLEMENTED_YET_MODE = 1004
    NO_THEMES_MODE = 1005

    MODE_NAMES = {
        DEPENDENCY_ERROR: 'DEPENDENCY_ERROR',
        NO_PLAYER_ERROR_MODE: 'NO_PLAYER_ERROR_MODE',
        NORMAL_MODE: 'NORMAL_MODE',
        PLAYLIST_MODE: 'PLAYLIST_MODE',
        SEARCH_NORMAL_MODE: 'SEARCH_NORMAL_MODE',
        SEARCH_PLAYLIST_MODE: 'SEARCH_PLAYLIST_MODE',
        SEARCH_THEME_MODE: 'SEARCH_THEME_MODE',
        SEARCH_SELECT_PLAYLIST_MODE: 'SEARCH_SELECT_PLAYLIST_MODE',
        SEARCH_SELECT_STATION_MODE: 'SEARCH_SELECT_STATION_MODE',
        CONFIG_MODE: 'CONFIG_MODE',
        SELECT_PLAYER_MODE: 'SELECT_PLAYER_MODE',
        SELECT_ENCODING_MODE: 'SELECT_ENCODING_MODE',
        SELECT_PLAYLIST_MODE: 'SELECT_PLAYLIST_MODE',
        SELECT_STATION_MODE: 'SELECT_STATION_MODE',
        SELECT_STATION_ENCODING_MODE: 'SELECT_STATION_ENCODING_MODE',
        EDIT_STATION_ENCODING_MODE: 'EDIT_STATION_ENCODING_MODE',
        NEW_THEME_MODE: 'NEW_THEME_MODE',
        EDIT_THEME_MODE: 'EDIT_THEME_MODE',
        REMOVE_STATION_MODE: 'REMOVE_STATION_MODE',
        REMOVE_GROUP_MODE: 'REMOVE_GROUP_MODE',
        SAVE_PLAYLIST_MODE: 'SAVE_PLAYLIST_MODE',
        ASK_TO_SAVE_PLAYLIST_WHEN_OPENING_PLAYLIST_MODE: 'ASK_TO_SAVE_PLAYLIST_WHEN_OPENING_PLAYLIST_MODE',
        ASK_TO_SAVE_PLAYLIST_WHEN_BACK_IN_HISTORY_MODE: 'ASK_TO_SAVE_PLAYLIST_WHEN_BACK_IN_HISTORY_MODE',
        ASK_TO_SAVE_PLAYLIST_WHEN_EXITING_MODE: 'ASK_TO_SAVE_PLAYLIST_WHEN_EXITING_MODE',
        MAIN_HELP_MODE: 'MAIN_HELP_MODE',
        MAIN_HELP_MODE_PAGE_2: 'MAIN_HELP_MODE_PAGE_2',
        MAIN_HELP_MODE_PAGE_3: 'MAIN_HELP_MODE_PAGE_3',
        MAIN_HELP_MODE_PAGE_4: 'MAIN_HELP_MODE_PAGE_4',
        MAIN_HELP_MODE_PAGE_5: 'MAIN_HELP_MODE_PAGE_5',
        PLAYLIST_HELP_MODE: 'PLAYLIST_HELP_MODE',
        CONFIG_HELP_MODE: 'CONFIG_HELP_MODE',
        THEME_HELP_MODE: 'THEME_HELP_MODE',
        SELECT_PLAYER_HELP_MODE: 'SELECT_PLAYER_HELP_MODE',
        SELECT_ENCODING_HELP_MODE: 'SELECT_ENCODING_HELP_MODE',
        SELECT_PLAYLIST_HELP_MODE: 'SELECT_PLAYLIST_HELP_MODE',
        SELECT_STATION_HELP_MODE: 'SELECT_STATION_HELP_MODE',
        NEW_THEME_HELP_MODE: 'NEW_THEME_HELP_MODE',
        EDIT_THEME_HELP_MODE: 'EDIT_THEME_HELP_MODE',
        ASK_TO_CREATE_NEW_THEME_MODE: 'ASK_TO_CREATE_NEW_THEME_MODE',
        SEARCH_HELP_MODE: 'SEARCH_HELP_MODE',
        PLAYLIST_RECOVERY_ERROR_MODE: 'PLAYLIST_RECOVERY_ERROR_MODE',
        PLAYLIST_NOT_FOUND_ERROR_MODE: 'PLAYLIST_NOT_FOUND_ERROR_MODE',
        PLAYLIST_LOAD_ERROR_MODE: 'PLAYLIST_LOAD_ERROR_MODE',
        PLAYLIST_RELOAD_ERROR_MODE: 'PLAYLIST_RELOAD_ERROR_MODE',
        PLAYLIST_RELOAD_CONFIRM_MODE: 'PLAYLIST_RELOAD_CONFIRM_MODE',
        PLAYLIST_DIRTY_RELOAD_CONFIRM_MODE: 'PLAYLIST_DIRTY_RELOAD_CONFIRM_MODE',
        PLAYLIST_SCAN_ERROR_MODE: 'PLAYLIST_SCAN_ERROR_MODE',
        SAVE_PLAYLIST_ERROR_1_MODE: 'SAVE_PLAYLIST_ERROR_1_MODE',
        SAVE_PLAYLIST_ERROR_2_MODE: 'SAVE_PLAYLIST_ERROR_2_MODE',
        FOREIGN_PLAYLIST_ASK_MODE: 'FOREIGN_PLAYLIST_ASK_MODE',
        FOREIGN_PLAYLIST_MESSAGE_MODE: 'FOREIGN_PLAYLIST_MESSAGE_MODE',
        FOREIGN_PLAYLIST_COPY_ERROR_MODE: 'FOREIGN_PLAYLIST_COPY_ERROR_MODE',
        CONFIG_SAVE_ERROR_MODE: 'CONFIG_SAVE_ERROR_MODE',
        THEME_MODE: 'THEME_MODE',
        UPDATE_NOTIFICATION_MODE: 'UPDATE_NOTIFICATION_MODE',
        UPDATE_NOTIFICATION_OK_MODE: 'UPDATE_NOTIFICATION_OK_MODE',
        UPDATE_NOTIFICATION_NOK_MODE: 'UPDATE_NOTIFICATION_NOK_MODE',
        SESSION_LOCKED_MODE: 'SESSION_LOCKED_MODE',
        NOT_IMPLEMENTED_YET_MODE: 'NOT_IMPLEMENTED_YET_MODE',
        ADD_STATION_MODE: 'ADD_STATION_MODE',
        EDIT_STATION_MODE: 'EDIT_STATION_MODE',
        LINE_EDITOR_HELP_MODE: 'LINE_EDITOR_HELP_MODE',
        EDIT_STATION_NAME_ERROR: 'EDIT_STATION_NAME_ERROR',
        EDIT_STATION_URL_ERROR: 'EDIT_STATION_URL_ERROR',
        EDIT_STATION_ICON_URL_ERROR: 'EDIT_STATION_ICON_URL_ERROR',
        EDIT_STATION_ICON_FORMAT_ERROR: 'EDIT_STATION_ICON_FORMAT_ERROR',
        PY2_EDITOR_ERROR: 'PY2_EDITOR_ERROR',
        REQUESTS_MODULE_NOT_INSTALLED_ERROR: 'REQUESTS_MODULE_NOT_INSTALLED_ERROR',
        NETIFACES_MODULE_NOT_INSTALLED_ERROR: 'NETIFACES_MODULE_NOT_INSTALLED_ERROR',
        UNKNOWN_BROWSER_SERVICE_ERROR: 'UNKNOWN_BROWSER_SERVICE_ERROR',
        SERVICE_CONNECTION_ERROR: 'SERVICE_CONNECTION_ERROR',
        PLAYER_CHANGED_INFO_MODE: 'PLAYER_CHANGED_INFO_MODE',
        HISTORY_EMPTY_NOTIFICATION: 'HISTORY_EMPTY_NOTIFICATION',
        REGISTER_SAVE_ERROR_MODE: 'REGISTER_SAVE_ERROR_MODE',
        CLEAR_REGISTER_MODE: 'CLEAR_REGISTER_MODE',
        CLEAR_ALL_REGISTERS_MODE: 'CLEAR_ALL_REGISTERS_MODE',
        REGISTER_HELP_MODE: 'REGISTER_HELP_MODE',
        EXTRA_COMMANDS_HELP_MODE: 'EXTRA_COMMANDS_HELP_MODE',
        YANK_HELP_MODE: 'YANK_HELP_MODE',
        STATION_INFO_MODE: 'STATION_INFO_MODE',
        STATION_DATABASE_INFO_MODE: 'STATION_DATABASE_INFO_MODE',
        STATION_INFO_ERROR_MODE: 'STATION_INFO_ERROR_MODE',
        CREATE_PLAYLIST_MODE: 'CREATE_PLAYLIST_MODE',
        RENAME_PLAYLIST_MODE: 'RENAME_PLAYLIST_MODE',
        PLAYLIST_COPY_ERROR: 'PLAYLIST_COPY_ERROR',
        PLAYLIST_RENAME_ERROR: 'PLAYLIST_RENAME_ERROR',
        PLAYLIST_CREATE_ERROR: 'PLAYLIST_CREATE_ERROR',
        PLAYLIST_NOT_SAVED_ERROR_MODE: 'PLAYLIST_NOT_SAVED_ERROR_MODE',
        CONNECTION_MODE: 'CONNECTION_MODE',
        PASTE_MODE: 'PASTE_MODE',
        UNNAMED_REGISTER_MODE: 'UNNAMED_REGISTER_MODE',
        PLAYER_PARAMS_MODE: 'PLAYER_PARAMS_MODE',
        MOUSE_RESTART_INFO_MODE: 'MOUSE_RESTART_INFO_MODE',
        IN_PLAYER_PARAMS_EDITOR: 'IN_PLAYER_PARAMS_EDITOR',
        IN_PLAYER_PARAMS_EDITOR_HELP_MODE: 'IN_PLAYER_PARAMS_EDITOR_HELP_MODE',
        USER_PARAMETER_ERROR: 'USER_PARAMETER_ERROR',
        VOTE_RESULT_MODE: 'VOTE_RESULT_MODE',
        BROWSER_SORT_MODE: 'BROWSER_SORT_MODE',
        BROWSER_SERVER_SELECTION_MODE: 'BROWSER_SERVER_SELECTION_MODE',
        BROWSER_SEARCH_MODE: 'BROWSER_SEARCH_MODE',
        NO_BROWSER_SEARCH_RESULT_NOTIFICATION: 'NO_BROWSER_SEARCH_RESULT_NOTIFICATION',
        BROWSER_OPEN_MODE: 'BROWSER_OPEN_MODE',
        RADIO_BROWSER_SEARCH_HELP_MODE: 'RADIO_BROWSER_SEARCH_HELP_MODE',
        RADIO_BROWSER_CONFIG_HELP_MODE: 'RADIO_BROWSER_CONFIG_HELP_MODE' ,
        BROWSER_PERFORMING_SEARCH_MODE: 'BROWSER_PERFORMING_SEARCH_MODE',
        ASK_TO_SAVE_BROWSER_CONFIG_FROM_BROWSER: 'ASK_TO_SAVE_BROWSER_CONFIG_FROM_BROWSER',
        ASK_TO_SAVE_BROWSER_CONFIG_FROM_CONFIG: 'ASK_TO_SAVE_BROWSER_CONFIG_FROM_CONFIG',
        ASK_TO_SAVE_BROWSER_CONFIG_TO_EXIT: 'ASK_TO_SAVE_BROWSER_CONFIG_TO_EXIT',
        RADIO_BROWSER_CONFIG_MODE: 'RADIO_BROWSER_CONFIG_MODE',
        BROWSER_CONFIG_SAVE_ERROR_MODE: 'BROWSER_CONFIG_SAVE_ERROR_MODE',
        SERVICE_SERVERS_UNREACHABLE: 'SERVICE_SERVERS_UNREACHABLE',
        WIN_MANAGE_PLAYERS_MSG_MODE: 'WIN_MANAGE_PLAYERS_MSG_MODE',
        WIN_PRINT_EXE_LOCATION_MODE: 'WIN_PRINT_EXE_LOCATION_MODE',
        WIN_UNINSTALL_MODE: 'WIN_UNINSTALL_MODE',
        WIN_REMOVE_OLD_INSTALLATION_MODE: 'WIN_REMOVE_OLD_INSTALLATION_MODE',
        SCHEDULE_EDIT_MODE: 'SCHEDULE_EDIT_MODE',
        SCHEDULE_EDIT_HELP_MODE: 'SCHEDULE_EDIT_HELP_MODE',
        SCHEDULE_PLAYER_SELECT_MODE: 'SCHEDULE_PLAYER_SELECT_MODE',
        SCHEDULE_STATION_SELECT_MODE: 'SCHEDULE_STATION_SELECT_MODE',
        NO_THEMES_MODE: 'NO_THEMES_MODE',
        REMOTE_CONTROL_SERVER_START_ERROR_MODE: 'REMOTE_CONTROL_SERVER_START_ERROR_MODE',
        REMOTE_CONTROL_SERVER_DEAD_ERROR_MODE: 'REMOTE_CONTROL_SERVER_DEAD_ERROR_MODE',
        REMOTE_CONTROL_SERVER_ACTIVE_MODE: 'REMOTE_CONTROL_SERVER_ACTIVE_MODE',
        REMOTE_CONTROL_SERVER_NOT_ACTIVE_MODE: 'REMOTE_CONTROL_SERVER_NOT_ACTIVE_MODE',
        REMOTE_CONTROL_SERVER_ERROR_MODE: 'REMOTE_CONTROL_SERVER_ERROR_MODE',
        CHANGE_PLAYER_MODE: 'CHANGE_PLAYER_MODE',
        CHANGE_PLAYER_ONE_PLAYER_ERROR_MODE: 'CHANGE_PLAYER_ONE_PLAYER_ERROR_MODE',
        CHANGE_PLAYER_SAME_PLAYER_ERROR_MODE: 'CHANGE_PLAYER_SAME_PLAYER_ERROR_MODE',
        ASK_TO_UPDATE_STATIONS_CSV_MODE: 'ASK_TO_UPDATE_STATIONS_CSV_MODE',
        UPDATE_NOTIFICATION_MODE: 'UPDATE_NOTIFICATION_MODE',
        UPDATE_STATIONS_CSV_RESULT_MODE: 'UPDATE_STATIONS_CSV_RESULT_MODE',
        GROUP_SELECTION_MODE: 'GROUP_SELECTION_MODE',
        GROUP_SEARCH_MODE: 'GROUP_SEARCH_MODE',
        GROUP_HELP_MODE: 'GROUP_HELP_MODE',
        RECORD_WINDOW_MODE: 'RECORD_WINDOW_MODE',
        WIN_VLC_NO_RECORD_MODE: 'WIN_VLC_NO_RECORD_MODE',
        BUFFER_SET_MODE: 'BUFFER_SET_MODE',
        SCHEDULE_ERROR_MODE: 'SCHEDULE_ERROR_MODE',
    }

    ''' When PASSIVE_WINDOWS target is one of them,
    also set window_mode '''
    MAIN_MODES = (
        NORMAL_MODE,
        PLAYLIST_MODE,
        CONFIG_MODE,
        ADD_STATION_MODE,
        EDIT_STATION_MODE,
    )

    FULL_SCREEN_MODES = (
        NORMAL_MODE,
        CONFIG_MODE,
        BROWSER_SEARCH_MODE,
        EDIT_STATION_MODE,
        ADD_STATION_MODE,
        RENAME_PLAYLIST_MODE,
        RADIO_BROWSER_CONFIG_MODE,
    )

    PASSIVE_WINDOWS = (
        SESSION_LOCKED_MODE,
        UPDATE_NOTIFICATION_NOK_MODE,
        MAIN_HELP_MODE,
        MAIN_HELP_MODE_PAGE_2,
        MAIN_HELP_MODE_PAGE_3,
        MAIN_HELP_MODE_PAGE_4,
        MAIN_HELP_MODE_PAGE_5,
        CONFIG_HELP_MODE,
        SELECT_PLAYER_HELP_MODE,
        SELECT_PLAYLIST_HELP_MODE,
        SELECT_STATION_HELP_MODE,
        PLAYLIST_RELOAD_ERROR_MODE,
        SAVE_PLAYLIST_ERROR_1_MODE,
        SAVE_PLAYLIST_ERROR_2_MODE,
        FOREIGN_PLAYLIST_MESSAGE_MODE,
        FOREIGN_PLAYLIST_COPY_ERROR_MODE,
        PLAYLIST_HELP_MODE,
        PLAYLIST_LOAD_ERROR_MODE,
        PLAYLIST_NOT_FOUND_ERROR_MODE,
        SELECT_ENCODING_HELP_MODE,
        THEME_HELP_MODE,
        SEARCH_HELP_MODE,
        LINE_EDITOR_HELP_MODE,
        EDIT_STATION_NAME_ERROR,
        EDIT_STATION_URL_ERROR,
        EDIT_STATION_ICON_URL_ERROR,
        EDIT_STATION_ICON_FORMAT_ERROR,
        PY2_EDITOR_ERROR,
        REQUESTS_MODULE_NOT_INSTALLED_ERROR,
        NETIFACES_MODULE_NOT_INSTALLED_ERROR,
        DNSPYTHON_MODULE_NOT_INSTALLED_ERROR,
        UNKNOWN_BROWSER_SERVICE_ERROR,
        SERVICE_CONNECTION_ERROR,
        PLAYER_CHANGED_INFO_MODE,
        REGISTER_SAVE_ERROR_MODE,
        REGISTER_HELP_MODE,
        EXTRA_COMMANDS_HELP_MODE,
        YANK_HELP_MODE,
        STATION_INFO_ERROR_MODE,
        PLAYLIST_COPY_ERROR,
        PLAYLIST_RENAME_ERROR,
        PLAYLIST_CREATE_ERROR,
        PLAYLIST_NOT_SAVED_ERROR_MODE,
        UNNAMED_REGISTER_MODE,
        MOUSE_RESTART_INFO_MODE,
        IN_PLAYER_PARAMS_EDITOR_HELP_MODE,
        USER_PARAMETER_ERROR,
        STATION_DATABASE_INFO_MODE,
        VOTE_RESULT_MODE,
        RADIO_BROWSER_SEARCH_HELP_MODE,
        RADIO_BROWSER_CONFIG_HELP_MODE,
        BROWSER_CONFIG_SAVE_ERROR_MODE,
        SERVICE_SERVERS_UNREACHABLE,
        SELECT_PLAYLIST_HELP_MODE,
        REMOTE_CONTROL_SERVER_START_ERROR_MODE,
        REMOTE_CONTROL_SERVER_DEAD_ERROR_MODE,
        REMOTE_CONTROL_SERVER_ERROR_MODE,
        CHANGE_PLAYER_ONE_PLAYER_ERROR_MODE,
        CHANGE_PLAYER_SAME_PLAYER_ERROR_MODE,
        UPDATE_STATIONS_CSV_RESULT_MODE,
        GROUP_HELP_MODE,
        WIN_VLC_NO_RECORD_MODE,
        SCHEDULE_EDIT_HELP_MODE,
        SCHEDULE_ERROR_MODE,
    )

    def __init__(self):
        pass


class Window_Stack(Window_Stack_Constants):
    _dq = deque()

    def __init__(self):
        super(Window_Stack_Constants, self).__init__()
        self._dq.append([self.NORMAL_MODE, self.NORMAL_MODE])

    def __del__(self):
        self._dq.clear()
        self._dq = None

    @property
    def operation_mode(self):
        return self._dq[-1][0]

    @operation_mode.setter
    def operation_mode(self, a_mode):
        if a_mode in self.MAIN_MODES:
            ''' also setting operation_mode in
                window_mode property setter
            '''
            self.window_mode = a_mode
        else:
            tmp = [a_mode, self._dq[-1][1]]
            if self._dq[-1] != tmp:
                self._dq.append([a_mode, self._dq[-1][1]])
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug('MODE: {0} -> {1} - {2}'.format(
                        self.mode_name(self._dq[-2][0]),
                        self.mode_name(self._dq[-1][0]),
                        list(self._dq)))
            else:
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug('MODE: Refusing to add duplicate {0} Remaining at {1}'.format(tmp, list(self._dq)))

    @property
    def window_mode(self):
        return self._dq[-1][1]

    @window_mode.setter
    def window_mode(self, a_mode):
        tmp = [a_mode, a_mode]
        if self._dq[-1] != tmp:
            self._dq.append([a_mode, a_mode])
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug('WIN MODE: {0} -> {1} - {2}'.format(
                    self.mode_name(self._dq[-2][0]),
                    self.mode_name(self._dq[-1][0]),
                    list(self._dq)))
        else:
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug('WIN MODE: Refusing to add duplicate {0} Remaining at {1}'.format(tmp, list(self._dq)))

    @property
    def previous_operation_mode(self):
        try:
            return self._dq[-2][0]
        except:
            return -2

    @previous_operation_mode.setter
    def previous_open_window(self, a_mode):
        return

    @property
    def previous_window_mode(self):
        return self._dq[-2][1]

    @previous_window_mode.setter
    def previous_window_mode(self, a_mode):
        return

    def str_to_mode(self, stringToFind):
        ''' return mode number when given mode name '''
        for item in self.MODE_NAMES.items():
            if item[1] == stringToFind:
                return item[0]
        return -2

    def str_to_mode_tuple(self, stringToFind):
        ''' return mode tuple when given mode name '''
        for item in self.MODE_NAMES.items():
            if item[1] == stringToFind:
                return item
        return -2, 'UNKNOWN'

    def mode_name(self, intToFind):
        if intToFind in self.MODE_NAMES.keys():
            return self.MODE_NAMES[intToFind]
        return 'UNKNOWN'

    def close_window(self):
        if len(self._dq) == 1 and self._dq[0] != [self.NORMAL_MODE, self.NORMAL_MODE]:
            self._dq[0] = [self.NORMAL_MODE, self.NORMAL_MODE]
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug('CLOSE MODE: Resetting...')

        if len(self._dq) > 1:
            tmp = self._dq.pop()
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug('CLOSE MODE: {0} -> {1} - {2}'.format(self.mode_name(tmp[0]), self.mode_name(self._dq[-1][0]), list(self._dq)))
        else:
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug('CLOSE MODE: Refusing to clear que...')
