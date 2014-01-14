# Copyright (c) 2014 The Chromium Embedded Framework Authors. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.
#
# ---------------------------------------------------------------------------
#
# This file was generated by the CEF translator tool and should not edited
# by hand. See the translator.README.txt file in the tools directory for
# more information.
#

{
  'variables': {
    'autogen_cpp_includes': [
      'include/cef_app.h',
      'include/cef_auth_callback.h',
      'include/cef_browser.h',
      'include/cef_browser_process_handler.h',
      'include/cef_callback.h',
      'include/cef_client.h',
      'include/cef_command_line.h',
      'include/cef_context_menu_handler.h',
      'include/cef_cookie.h',
      'include/cef_dialog_handler.h',
      'include/cef_display_handler.h',
      'include/cef_dom.h',
      'include/cef_download_handler.h',
      'include/cef_download_item.h',
      'include/cef_drag_data.h',
      'include/cef_drag_handler.h',
      'include/cef_focus_handler.h',
      'include/cef_frame.h',
      'include/cef_geolocation.h',
      'include/cef_geolocation_handler.h',
      'include/cef_jsdialog_handler.h',
      'include/cef_keyboard_handler.h',
      'include/cef_life_span_handler.h',
      'include/cef_load_handler.h',
      'include/cef_menu_model.h',
      'include/cef_origin_whitelist.h',
      'include/cef_path_util.h',
      'include/cef_process_message.h',
      'include/cef_process_util.h',
      'include/cef_render_handler.h',
      'include/cef_render_process_handler.h',
      'include/cef_request.h',
      'include/cef_request_context.h',
      'include/cef_request_context_handler.h',
      'include/cef_request_handler.h',
      'include/cef_resource_bundle_handler.h',
      'include/cef_resource_handler.h',
      'include/cef_response.h',
      'include/cef_scheme.h',
      'include/cef_stream.h',
      'include/cef_string_visitor.h',
      'include/cef_task.h',
      'include/cef_trace.h',
      'include/cef_url.h',
      'include/cef_urlrequest.h',
      'include/cef_v8.h',
      'include/cef_values.h',
      'include/cef_web_plugin.h',
      'include/cef_xml_reader.h',
      'include/cef_zip_reader.h',
    ],
    'autogen_capi_includes': [
      'include/capi/cef_app_capi.h',
      'include/capi/cef_auth_callback_capi.h',
      'include/capi/cef_browser_capi.h',
      'include/capi/cef_browser_process_handler_capi.h',
      'include/capi/cef_callback_capi.h',
      'include/capi/cef_client_capi.h',
      'include/capi/cef_command_line_capi.h',
      'include/capi/cef_context_menu_handler_capi.h',
      'include/capi/cef_cookie_capi.h',
      'include/capi/cef_dialog_handler_capi.h',
      'include/capi/cef_display_handler_capi.h',
      'include/capi/cef_dom_capi.h',
      'include/capi/cef_download_handler_capi.h',
      'include/capi/cef_download_item_capi.h',
      'include/capi/cef_drag_data_capi.h',
      'include/capi/cef_drag_handler_capi.h',
      'include/capi/cef_focus_handler_capi.h',
      'include/capi/cef_frame_capi.h',
      'include/capi/cef_geolocation_capi.h',
      'include/capi/cef_geolocation_handler_capi.h',
      'include/capi/cef_jsdialog_handler_capi.h',
      'include/capi/cef_keyboard_handler_capi.h',
      'include/capi/cef_life_span_handler_capi.h',
      'include/capi/cef_load_handler_capi.h',
      'include/capi/cef_menu_model_capi.h',
      'include/capi/cef_origin_whitelist_capi.h',
      'include/capi/cef_path_util_capi.h',
      'include/capi/cef_process_message_capi.h',
      'include/capi/cef_process_util_capi.h',
      'include/capi/cef_render_handler_capi.h',
      'include/capi/cef_render_process_handler_capi.h',
      'include/capi/cef_request_capi.h',
      'include/capi/cef_request_context_capi.h',
      'include/capi/cef_request_context_handler_capi.h',
      'include/capi/cef_request_handler_capi.h',
      'include/capi/cef_resource_bundle_handler_capi.h',
      'include/capi/cef_resource_handler_capi.h',
      'include/capi/cef_response_capi.h',
      'include/capi/cef_scheme_capi.h',
      'include/capi/cef_stream_capi.h',
      'include/capi/cef_string_visitor_capi.h',
      'include/capi/cef_task_capi.h',
      'include/capi/cef_trace_capi.h',
      'include/capi/cef_url_capi.h',
      'include/capi/cef_urlrequest_capi.h',
      'include/capi/cef_v8_capi.h',
      'include/capi/cef_values_capi.h',
      'include/capi/cef_web_plugin_capi.h',
      'include/capi/cef_xml_reader_capi.h',
      'include/capi/cef_zip_reader_capi.h',
    ],
    'autogen_library_side': [
      'libcef_dll/cpptoc/allow_certificate_error_callback_cpptoc.cc',
      'libcef_dll/cpptoc/allow_certificate_error_callback_cpptoc.h',
      'libcef_dll/ctocpp/app_ctocpp.cc',
      'libcef_dll/ctocpp/app_ctocpp.h',
      'libcef_dll/cpptoc/auth_callback_cpptoc.cc',
      'libcef_dll/cpptoc/auth_callback_cpptoc.h',
      'libcef_dll/cpptoc/before_download_callback_cpptoc.cc',
      'libcef_dll/cpptoc/before_download_callback_cpptoc.h',
      'libcef_dll/cpptoc/binary_value_cpptoc.cc',
      'libcef_dll/cpptoc/binary_value_cpptoc.h',
      'libcef_dll/cpptoc/browser_cpptoc.cc',
      'libcef_dll/cpptoc/browser_cpptoc.h',
      'libcef_dll/cpptoc/browser_host_cpptoc.cc',
      'libcef_dll/cpptoc/browser_host_cpptoc.h',
      'libcef_dll/ctocpp/browser_process_handler_ctocpp.cc',
      'libcef_dll/ctocpp/browser_process_handler_ctocpp.h',
      'libcef_dll/cpptoc/callback_cpptoc.cc',
      'libcef_dll/cpptoc/callback_cpptoc.h',
      'libcef_dll/ctocpp/client_ctocpp.cc',
      'libcef_dll/ctocpp/client_ctocpp.h',
      'libcef_dll/cpptoc/command_line_cpptoc.cc',
      'libcef_dll/cpptoc/command_line_cpptoc.h',
      'libcef_dll/ctocpp/completion_handler_ctocpp.cc',
      'libcef_dll/ctocpp/completion_handler_ctocpp.h',
      'libcef_dll/ctocpp/context_menu_handler_ctocpp.cc',
      'libcef_dll/ctocpp/context_menu_handler_ctocpp.h',
      'libcef_dll/cpptoc/context_menu_params_cpptoc.cc',
      'libcef_dll/cpptoc/context_menu_params_cpptoc.h',
      'libcef_dll/cpptoc/cookie_manager_cpptoc.cc',
      'libcef_dll/cpptoc/cookie_manager_cpptoc.h',
      'libcef_dll/ctocpp/cookie_visitor_ctocpp.cc',
      'libcef_dll/ctocpp/cookie_visitor_ctocpp.h',
      'libcef_dll/cpptoc/domdocument_cpptoc.cc',
      'libcef_dll/cpptoc/domdocument_cpptoc.h',
      'libcef_dll/cpptoc/domevent_cpptoc.cc',
      'libcef_dll/cpptoc/domevent_cpptoc.h',
      'libcef_dll/ctocpp/domevent_listener_ctocpp.cc',
      'libcef_dll/ctocpp/domevent_listener_ctocpp.h',
      'libcef_dll/cpptoc/domnode_cpptoc.cc',
      'libcef_dll/cpptoc/domnode_cpptoc.h',
      'libcef_dll/ctocpp/domvisitor_ctocpp.cc',
      'libcef_dll/ctocpp/domvisitor_ctocpp.h',
      'libcef_dll/ctocpp/dialog_handler_ctocpp.cc',
      'libcef_dll/ctocpp/dialog_handler_ctocpp.h',
      'libcef_dll/cpptoc/dictionary_value_cpptoc.cc',
      'libcef_dll/cpptoc/dictionary_value_cpptoc.h',
      'libcef_dll/ctocpp/display_handler_ctocpp.cc',
      'libcef_dll/ctocpp/display_handler_ctocpp.h',
      'libcef_dll/ctocpp/download_handler_ctocpp.cc',
      'libcef_dll/ctocpp/download_handler_ctocpp.h',
      'libcef_dll/cpptoc/download_item_cpptoc.cc',
      'libcef_dll/cpptoc/download_item_cpptoc.h',
      'libcef_dll/cpptoc/download_item_callback_cpptoc.cc',
      'libcef_dll/cpptoc/download_item_callback_cpptoc.h',
      'libcef_dll/cpptoc/drag_data_cpptoc.cc',
      'libcef_dll/cpptoc/drag_data_cpptoc.h',
      'libcef_dll/ctocpp/drag_handler_ctocpp.cc',
      'libcef_dll/ctocpp/drag_handler_ctocpp.h',
      'libcef_dll/cpptoc/file_dialog_callback_cpptoc.cc',
      'libcef_dll/cpptoc/file_dialog_callback_cpptoc.h',
      'libcef_dll/ctocpp/focus_handler_ctocpp.cc',
      'libcef_dll/ctocpp/focus_handler_ctocpp.h',
      'libcef_dll/cpptoc/frame_cpptoc.cc',
      'libcef_dll/cpptoc/frame_cpptoc.h',
      'libcef_dll/cpptoc/geolocation_callback_cpptoc.cc',
      'libcef_dll/cpptoc/geolocation_callback_cpptoc.h',
      'libcef_dll/ctocpp/geolocation_handler_ctocpp.cc',
      'libcef_dll/ctocpp/geolocation_handler_ctocpp.h',
      'libcef_dll/ctocpp/get_geolocation_callback_ctocpp.cc',
      'libcef_dll/ctocpp/get_geolocation_callback_ctocpp.h',
      'libcef_dll/cpptoc/jsdialog_callback_cpptoc.cc',
      'libcef_dll/cpptoc/jsdialog_callback_cpptoc.h',
      'libcef_dll/ctocpp/jsdialog_handler_ctocpp.cc',
      'libcef_dll/ctocpp/jsdialog_handler_ctocpp.h',
      'libcef_dll/ctocpp/keyboard_handler_ctocpp.cc',
      'libcef_dll/ctocpp/keyboard_handler_ctocpp.h',
      'libcef_dll/ctocpp/life_span_handler_ctocpp.cc',
      'libcef_dll/ctocpp/life_span_handler_ctocpp.h',
      'libcef_dll/cpptoc/list_value_cpptoc.cc',
      'libcef_dll/cpptoc/list_value_cpptoc.h',
      'libcef_dll/ctocpp/load_handler_ctocpp.cc',
      'libcef_dll/ctocpp/load_handler_ctocpp.h',
      'libcef_dll/cpptoc/menu_model_cpptoc.cc',
      'libcef_dll/cpptoc/menu_model_cpptoc.h',
      'libcef_dll/cpptoc/post_data_cpptoc.cc',
      'libcef_dll/cpptoc/post_data_cpptoc.h',
      'libcef_dll/cpptoc/post_data_element_cpptoc.cc',
      'libcef_dll/cpptoc/post_data_element_cpptoc.h',
      'libcef_dll/cpptoc/process_message_cpptoc.cc',
      'libcef_dll/cpptoc/process_message_cpptoc.h',
      'libcef_dll/cpptoc/quota_callback_cpptoc.cc',
      'libcef_dll/cpptoc/quota_callback_cpptoc.h',
      'libcef_dll/ctocpp/read_handler_ctocpp.cc',
      'libcef_dll/ctocpp/read_handler_ctocpp.h',
      'libcef_dll/ctocpp/render_handler_ctocpp.cc',
      'libcef_dll/ctocpp/render_handler_ctocpp.h',
      'libcef_dll/ctocpp/render_process_handler_ctocpp.cc',
      'libcef_dll/ctocpp/render_process_handler_ctocpp.h',
      'libcef_dll/cpptoc/request_cpptoc.cc',
      'libcef_dll/cpptoc/request_cpptoc.h',
      'libcef_dll/cpptoc/request_context_cpptoc.cc',
      'libcef_dll/cpptoc/request_context_cpptoc.h',
      'libcef_dll/ctocpp/request_context_handler_ctocpp.cc',
      'libcef_dll/ctocpp/request_context_handler_ctocpp.h',
      'libcef_dll/ctocpp/request_handler_ctocpp.cc',
      'libcef_dll/ctocpp/request_handler_ctocpp.h',
      'libcef_dll/ctocpp/resource_bundle_handler_ctocpp.cc',
      'libcef_dll/ctocpp/resource_bundle_handler_ctocpp.h',
      'libcef_dll/ctocpp/resource_handler_ctocpp.cc',
      'libcef_dll/ctocpp/resource_handler_ctocpp.h',
      'libcef_dll/cpptoc/response_cpptoc.cc',
      'libcef_dll/cpptoc/response_cpptoc.h',
      'libcef_dll/ctocpp/run_file_dialog_callback_ctocpp.cc',
      'libcef_dll/ctocpp/run_file_dialog_callback_ctocpp.h',
      'libcef_dll/ctocpp/scheme_handler_factory_ctocpp.cc',
      'libcef_dll/ctocpp/scheme_handler_factory_ctocpp.h',
      'libcef_dll/cpptoc/scheme_registrar_cpptoc.cc',
      'libcef_dll/cpptoc/scheme_registrar_cpptoc.h',
      'libcef_dll/cpptoc/stream_reader_cpptoc.cc',
      'libcef_dll/cpptoc/stream_reader_cpptoc.h',
      'libcef_dll/cpptoc/stream_writer_cpptoc.cc',
      'libcef_dll/cpptoc/stream_writer_cpptoc.h',
      'libcef_dll/ctocpp/string_visitor_ctocpp.cc',
      'libcef_dll/ctocpp/string_visitor_ctocpp.h',
      'libcef_dll/ctocpp/task_ctocpp.cc',
      'libcef_dll/ctocpp/task_ctocpp.h',
      'libcef_dll/cpptoc/task_runner_cpptoc.cc',
      'libcef_dll/cpptoc/task_runner_cpptoc.h',
      'libcef_dll/ctocpp/trace_client_ctocpp.cc',
      'libcef_dll/ctocpp/trace_client_ctocpp.h',
      'libcef_dll/cpptoc/urlrequest_cpptoc.cc',
      'libcef_dll/cpptoc/urlrequest_cpptoc.h',
      'libcef_dll/ctocpp/urlrequest_client_ctocpp.cc',
      'libcef_dll/ctocpp/urlrequest_client_ctocpp.h',
      'libcef_dll/ctocpp/v8accessor_ctocpp.cc',
      'libcef_dll/ctocpp/v8accessor_ctocpp.h',
      'libcef_dll/cpptoc/v8context_cpptoc.cc',
      'libcef_dll/cpptoc/v8context_cpptoc.h',
      'libcef_dll/cpptoc/v8exception_cpptoc.cc',
      'libcef_dll/cpptoc/v8exception_cpptoc.h',
      'libcef_dll/ctocpp/v8handler_ctocpp.cc',
      'libcef_dll/ctocpp/v8handler_ctocpp.h',
      'libcef_dll/cpptoc/v8stack_frame_cpptoc.cc',
      'libcef_dll/cpptoc/v8stack_frame_cpptoc.h',
      'libcef_dll/cpptoc/v8stack_trace_cpptoc.cc',
      'libcef_dll/cpptoc/v8stack_trace_cpptoc.h',
      'libcef_dll/cpptoc/v8value_cpptoc.cc',
      'libcef_dll/cpptoc/v8value_cpptoc.h',
      'libcef_dll/cpptoc/web_plugin_info_cpptoc.cc',
      'libcef_dll/cpptoc/web_plugin_info_cpptoc.h',
      'libcef_dll/ctocpp/web_plugin_info_visitor_ctocpp.cc',
      'libcef_dll/ctocpp/web_plugin_info_visitor_ctocpp.h',
      'libcef_dll/ctocpp/web_plugin_unstable_callback_ctocpp.cc',
      'libcef_dll/ctocpp/web_plugin_unstable_callback_ctocpp.h',
      'libcef_dll/ctocpp/write_handler_ctocpp.cc',
      'libcef_dll/ctocpp/write_handler_ctocpp.h',
      'libcef_dll/cpptoc/xml_reader_cpptoc.cc',
      'libcef_dll/cpptoc/xml_reader_cpptoc.h',
      'libcef_dll/cpptoc/zip_reader_cpptoc.cc',
      'libcef_dll/cpptoc/zip_reader_cpptoc.h',
    ],
    'autogen_client_side': [
      'libcef_dll/ctocpp/allow_certificate_error_callback_ctocpp.cc',
      'libcef_dll/ctocpp/allow_certificate_error_callback_ctocpp.h',
      'libcef_dll/cpptoc/app_cpptoc.cc',
      'libcef_dll/cpptoc/app_cpptoc.h',
      'libcef_dll/ctocpp/auth_callback_ctocpp.cc',
      'libcef_dll/ctocpp/auth_callback_ctocpp.h',
      'libcef_dll/ctocpp/before_download_callback_ctocpp.cc',
      'libcef_dll/ctocpp/before_download_callback_ctocpp.h',
      'libcef_dll/ctocpp/binary_value_ctocpp.cc',
      'libcef_dll/ctocpp/binary_value_ctocpp.h',
      'libcef_dll/ctocpp/browser_ctocpp.cc',
      'libcef_dll/ctocpp/browser_ctocpp.h',
      'libcef_dll/ctocpp/browser_host_ctocpp.cc',
      'libcef_dll/ctocpp/browser_host_ctocpp.h',
      'libcef_dll/cpptoc/browser_process_handler_cpptoc.cc',
      'libcef_dll/cpptoc/browser_process_handler_cpptoc.h',
      'libcef_dll/ctocpp/callback_ctocpp.cc',
      'libcef_dll/ctocpp/callback_ctocpp.h',
      'libcef_dll/cpptoc/client_cpptoc.cc',
      'libcef_dll/cpptoc/client_cpptoc.h',
      'libcef_dll/ctocpp/command_line_ctocpp.cc',
      'libcef_dll/ctocpp/command_line_ctocpp.h',
      'libcef_dll/cpptoc/completion_handler_cpptoc.cc',
      'libcef_dll/cpptoc/completion_handler_cpptoc.h',
      'libcef_dll/cpptoc/context_menu_handler_cpptoc.cc',
      'libcef_dll/cpptoc/context_menu_handler_cpptoc.h',
      'libcef_dll/ctocpp/context_menu_params_ctocpp.cc',
      'libcef_dll/ctocpp/context_menu_params_ctocpp.h',
      'libcef_dll/ctocpp/cookie_manager_ctocpp.cc',
      'libcef_dll/ctocpp/cookie_manager_ctocpp.h',
      'libcef_dll/cpptoc/cookie_visitor_cpptoc.cc',
      'libcef_dll/cpptoc/cookie_visitor_cpptoc.h',
      'libcef_dll/ctocpp/domdocument_ctocpp.cc',
      'libcef_dll/ctocpp/domdocument_ctocpp.h',
      'libcef_dll/ctocpp/domevent_ctocpp.cc',
      'libcef_dll/ctocpp/domevent_ctocpp.h',
      'libcef_dll/cpptoc/domevent_listener_cpptoc.cc',
      'libcef_dll/cpptoc/domevent_listener_cpptoc.h',
      'libcef_dll/ctocpp/domnode_ctocpp.cc',
      'libcef_dll/ctocpp/domnode_ctocpp.h',
      'libcef_dll/cpptoc/domvisitor_cpptoc.cc',
      'libcef_dll/cpptoc/domvisitor_cpptoc.h',
      'libcef_dll/cpptoc/dialog_handler_cpptoc.cc',
      'libcef_dll/cpptoc/dialog_handler_cpptoc.h',
      'libcef_dll/ctocpp/dictionary_value_ctocpp.cc',
      'libcef_dll/ctocpp/dictionary_value_ctocpp.h',
      'libcef_dll/cpptoc/display_handler_cpptoc.cc',
      'libcef_dll/cpptoc/display_handler_cpptoc.h',
      'libcef_dll/cpptoc/download_handler_cpptoc.cc',
      'libcef_dll/cpptoc/download_handler_cpptoc.h',
      'libcef_dll/ctocpp/download_item_ctocpp.cc',
      'libcef_dll/ctocpp/download_item_ctocpp.h',
      'libcef_dll/ctocpp/download_item_callback_ctocpp.cc',
      'libcef_dll/ctocpp/download_item_callback_ctocpp.h',
      'libcef_dll/ctocpp/drag_data_ctocpp.cc',
      'libcef_dll/ctocpp/drag_data_ctocpp.h',
      'libcef_dll/cpptoc/drag_handler_cpptoc.cc',
      'libcef_dll/cpptoc/drag_handler_cpptoc.h',
      'libcef_dll/ctocpp/file_dialog_callback_ctocpp.cc',
      'libcef_dll/ctocpp/file_dialog_callback_ctocpp.h',
      'libcef_dll/cpptoc/focus_handler_cpptoc.cc',
      'libcef_dll/cpptoc/focus_handler_cpptoc.h',
      'libcef_dll/ctocpp/frame_ctocpp.cc',
      'libcef_dll/ctocpp/frame_ctocpp.h',
      'libcef_dll/ctocpp/geolocation_callback_ctocpp.cc',
      'libcef_dll/ctocpp/geolocation_callback_ctocpp.h',
      'libcef_dll/cpptoc/geolocation_handler_cpptoc.cc',
      'libcef_dll/cpptoc/geolocation_handler_cpptoc.h',
      'libcef_dll/cpptoc/get_geolocation_callback_cpptoc.cc',
      'libcef_dll/cpptoc/get_geolocation_callback_cpptoc.h',
      'libcef_dll/ctocpp/jsdialog_callback_ctocpp.cc',
      'libcef_dll/ctocpp/jsdialog_callback_ctocpp.h',
      'libcef_dll/cpptoc/jsdialog_handler_cpptoc.cc',
      'libcef_dll/cpptoc/jsdialog_handler_cpptoc.h',
      'libcef_dll/cpptoc/keyboard_handler_cpptoc.cc',
      'libcef_dll/cpptoc/keyboard_handler_cpptoc.h',
      'libcef_dll/cpptoc/life_span_handler_cpptoc.cc',
      'libcef_dll/cpptoc/life_span_handler_cpptoc.h',
      'libcef_dll/ctocpp/list_value_ctocpp.cc',
      'libcef_dll/ctocpp/list_value_ctocpp.h',
      'libcef_dll/cpptoc/load_handler_cpptoc.cc',
      'libcef_dll/cpptoc/load_handler_cpptoc.h',
      'libcef_dll/ctocpp/menu_model_ctocpp.cc',
      'libcef_dll/ctocpp/menu_model_ctocpp.h',
      'libcef_dll/ctocpp/post_data_ctocpp.cc',
      'libcef_dll/ctocpp/post_data_ctocpp.h',
      'libcef_dll/ctocpp/post_data_element_ctocpp.cc',
      'libcef_dll/ctocpp/post_data_element_ctocpp.h',
      'libcef_dll/ctocpp/process_message_ctocpp.cc',
      'libcef_dll/ctocpp/process_message_ctocpp.h',
      'libcef_dll/ctocpp/quota_callback_ctocpp.cc',
      'libcef_dll/ctocpp/quota_callback_ctocpp.h',
      'libcef_dll/cpptoc/read_handler_cpptoc.cc',
      'libcef_dll/cpptoc/read_handler_cpptoc.h',
      'libcef_dll/cpptoc/render_handler_cpptoc.cc',
      'libcef_dll/cpptoc/render_handler_cpptoc.h',
      'libcef_dll/cpptoc/render_process_handler_cpptoc.cc',
      'libcef_dll/cpptoc/render_process_handler_cpptoc.h',
      'libcef_dll/ctocpp/request_ctocpp.cc',
      'libcef_dll/ctocpp/request_ctocpp.h',
      'libcef_dll/ctocpp/request_context_ctocpp.cc',
      'libcef_dll/ctocpp/request_context_ctocpp.h',
      'libcef_dll/cpptoc/request_context_handler_cpptoc.cc',
      'libcef_dll/cpptoc/request_context_handler_cpptoc.h',
      'libcef_dll/cpptoc/request_handler_cpptoc.cc',
      'libcef_dll/cpptoc/request_handler_cpptoc.h',
      'libcef_dll/cpptoc/resource_bundle_handler_cpptoc.cc',
      'libcef_dll/cpptoc/resource_bundle_handler_cpptoc.h',
      'libcef_dll/cpptoc/resource_handler_cpptoc.cc',
      'libcef_dll/cpptoc/resource_handler_cpptoc.h',
      'libcef_dll/ctocpp/response_ctocpp.cc',
      'libcef_dll/ctocpp/response_ctocpp.h',
      'libcef_dll/cpptoc/run_file_dialog_callback_cpptoc.cc',
      'libcef_dll/cpptoc/run_file_dialog_callback_cpptoc.h',
      'libcef_dll/cpptoc/scheme_handler_factory_cpptoc.cc',
      'libcef_dll/cpptoc/scheme_handler_factory_cpptoc.h',
      'libcef_dll/ctocpp/scheme_registrar_ctocpp.cc',
      'libcef_dll/ctocpp/scheme_registrar_ctocpp.h',
      'libcef_dll/ctocpp/stream_reader_ctocpp.cc',
      'libcef_dll/ctocpp/stream_reader_ctocpp.h',
      'libcef_dll/ctocpp/stream_writer_ctocpp.cc',
      'libcef_dll/ctocpp/stream_writer_ctocpp.h',
      'libcef_dll/cpptoc/string_visitor_cpptoc.cc',
      'libcef_dll/cpptoc/string_visitor_cpptoc.h',
      'libcef_dll/cpptoc/task_cpptoc.cc',
      'libcef_dll/cpptoc/task_cpptoc.h',
      'libcef_dll/ctocpp/task_runner_ctocpp.cc',
      'libcef_dll/ctocpp/task_runner_ctocpp.h',
      'libcef_dll/cpptoc/trace_client_cpptoc.cc',
      'libcef_dll/cpptoc/trace_client_cpptoc.h',
      'libcef_dll/ctocpp/urlrequest_ctocpp.cc',
      'libcef_dll/ctocpp/urlrequest_ctocpp.h',
      'libcef_dll/cpptoc/urlrequest_client_cpptoc.cc',
      'libcef_dll/cpptoc/urlrequest_client_cpptoc.h',
      'libcef_dll/cpptoc/v8accessor_cpptoc.cc',
      'libcef_dll/cpptoc/v8accessor_cpptoc.h',
      'libcef_dll/ctocpp/v8context_ctocpp.cc',
      'libcef_dll/ctocpp/v8context_ctocpp.h',
      'libcef_dll/ctocpp/v8exception_ctocpp.cc',
      'libcef_dll/ctocpp/v8exception_ctocpp.h',
      'libcef_dll/cpptoc/v8handler_cpptoc.cc',
      'libcef_dll/cpptoc/v8handler_cpptoc.h',
      'libcef_dll/ctocpp/v8stack_frame_ctocpp.cc',
      'libcef_dll/ctocpp/v8stack_frame_ctocpp.h',
      'libcef_dll/ctocpp/v8stack_trace_ctocpp.cc',
      'libcef_dll/ctocpp/v8stack_trace_ctocpp.h',
      'libcef_dll/ctocpp/v8value_ctocpp.cc',
      'libcef_dll/ctocpp/v8value_ctocpp.h',
      'libcef_dll/ctocpp/web_plugin_info_ctocpp.cc',
      'libcef_dll/ctocpp/web_plugin_info_ctocpp.h',
      'libcef_dll/cpptoc/web_plugin_info_visitor_cpptoc.cc',
      'libcef_dll/cpptoc/web_plugin_info_visitor_cpptoc.h',
      'libcef_dll/cpptoc/web_plugin_unstable_callback_cpptoc.cc',
      'libcef_dll/cpptoc/web_plugin_unstable_callback_cpptoc.h',
      'libcef_dll/cpptoc/write_handler_cpptoc.cc',
      'libcef_dll/cpptoc/write_handler_cpptoc.h',
      'libcef_dll/ctocpp/xml_reader_ctocpp.cc',
      'libcef_dll/ctocpp/xml_reader_ctocpp.h',
      'libcef_dll/ctocpp/zip_reader_ctocpp.cc',
      'libcef_dll/ctocpp/zip_reader_ctocpp.h',
    ],
  },
}
