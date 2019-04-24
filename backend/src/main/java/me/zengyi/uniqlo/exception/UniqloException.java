package me.zengyi.uniqlo.exception;

public class UniqloException extends RuntimeException {

    private static final long serialVersionUID = -3929875994748642627L;

    public UniqloException(String message) {
        super(message);
    }
}
