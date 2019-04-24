package me.zengyi.uniqlo.exception;

public class BadRequestException extends RuntimeException {

    private static final long serialVersionUID = -6594726112878311297L;

    public BadRequestException(String message) {
        super(message);
    }
}
