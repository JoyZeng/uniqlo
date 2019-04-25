package me.zengyi.uniqlo.common;

import java.util.HashMap;

public class APIResponse extends HashMap<String, Object> {

    private static final long serialVersionUID = 7413154911246858714L;

    public APIResponse success(Object result) {
        this.put("code", Constant.API_RESPONSE_CODE_SUCCESS);
        this.put("status", Constant.API_RESPONSE_STATUS_OK);
        this.put("message", "");
        this.put("result", result);
        return this;
    }

    public APIResponse failure(Integer code, String message, Object result) {
        this.put("code", code);
        this.put("status", Constant.API_RESPONSE_STATUS_ERROR);
        this.put("message", message);
        this.put("result", result);
        return this;
    }
}
