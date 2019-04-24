package me.zengyi.uniqlo.exception;

import lombok.extern.slf4j.Slf4j;
import me.zengyi.uniqlo.common.APIResponse;
import me.zengyi.uniqlo.common.Constant;
import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@Slf4j
@RestControllerAdvice
@Order(value = Ordered.HIGHEST_PRECEDENCE)
public class GlobalExceptionHandler {

    /**
     * Handle server internal error
     * @param e Exception
     * @return APIResponse
     */
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public APIResponse handleException(Exception e) {
        log.error("Server internal error: ", e);
        return new APIResponse()
                .failure(Constant.API_RESPONSE_CODE_SERVER_ERROR, "Server internal error", null);
    }

    /**
     * Handle application error
     * @param e UniqloException
     * @return APIResponse
     */
    @ExceptionHandler(UniqloException.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public APIResponse handleUniqloException(UniqloException e) {
        log.error("Application failure: {}", e.getMessage());
        return new APIResponse()
                .failure(Constant.API_RESPONSE_CODE_SERVER_ERROR, e.getMessage(), null);
    }

    /**
     * Handle invalid request
     * @param e BadRequestException
     * @return APIResponse
     */
    @ExceptionHandler(BadRequestException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public APIResponse handleBadRequestException(BadRequestException e) {
        log.error("Bad request: {}", e.getMessage());
        return new APIResponse()
                .failure(Constant.API_RESPONSE_CODE_BAD_REQUEST, e.getMessage(), null);
    }

}
