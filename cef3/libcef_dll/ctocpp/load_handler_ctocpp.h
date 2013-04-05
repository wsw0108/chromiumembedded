// Copyright (c) 2013 The Chromium Embedded Framework Authors. All rights
// reserved. Use of this source code is governed by a BSD-style license that
// can be found in the LICENSE file.
//
// ---------------------------------------------------------------------------
//
// This file was generated by the CEF translator tool. If making changes by
// hand only do so within the body of existing method and function
// implementations. See the translator.README.txt file in the tools directory
// for more information.
//

#ifndef CEF_LIBCEF_DLL_CTOCPP_LOAD_HANDLER_CTOCPP_H_
#define CEF_LIBCEF_DLL_CTOCPP_LOAD_HANDLER_CTOCPP_H_
#pragma once

#ifndef BUILDING_CEF_SHARED
#pragma message("Warning: "__FILE__" may be accessed DLL-side only")
#else  // BUILDING_CEF_SHARED

#include "include/cef_load_handler.h"
#include "include/capi/cef_load_handler_capi.h"
#include "libcef_dll/ctocpp/ctocpp.h"

// Wrap a C structure with a C++ class.
// This class may be instantiated and accessed DLL-side only.
class CefLoadHandlerCToCpp
    : public CefCToCpp<CefLoadHandlerCToCpp, CefLoadHandler,
        cef_load_handler_t> {
 public:
  explicit CefLoadHandlerCToCpp(cef_load_handler_t* str)
      : CefCToCpp<CefLoadHandlerCToCpp, CefLoadHandler, cef_load_handler_t>(
          str) {}
  virtual ~CefLoadHandlerCToCpp() {}

  // CefLoadHandler methods
  virtual void OnLoadStart(CefRefPtr<CefBrowser> browser,
      CefRefPtr<CefFrame> frame) OVERRIDE;
  virtual void OnLoadEnd(CefRefPtr<CefBrowser> browser,
      CefRefPtr<CefFrame> frame, int httpStatusCode) OVERRIDE;
  virtual void OnLoadError(CefRefPtr<CefBrowser> browser,
      CefRefPtr<CefFrame> frame, ErrorCode errorCode,
      const CefString& errorText, const CefString& failedUrl) OVERRIDE;
  virtual void OnRenderProcessTerminated(CefRefPtr<CefBrowser> browser,
      TerminationStatus status) OVERRIDE;
  virtual void OnPluginCrashed(CefRefPtr<CefBrowser> browser,
      const CefString& plugin_path) OVERRIDE;
};

#endif  // BUILDING_CEF_SHARED
#endif  // CEF_LIBCEF_DLL_CTOCPP_LOAD_HANDLER_CTOCPP_H_

