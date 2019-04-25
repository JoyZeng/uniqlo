package me.zengyi.uniqlo.controller;

import lombok.extern.slf4j.Slf4j;
import me.zengyi.uniqlo.common.APIResponse;
import me.zengyi.uniqlo.exception.UniqloException;
import me.zengyi.uniqlo.model.User;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.AuthenticationException;
import org.apache.shiro.authc.IncorrectCredentialsException;
import org.apache.shiro.authc.UnknownAccountException;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.subject.Subject;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import javax.validation.constraints.NotBlank;


@Slf4j
@RestController
public class LoginController {

    @PostMapping("/login")
    public APIResponse login(@NotBlank(message = "{required}") String userName,
                             @NotBlank(message = "{required}") String password, HttpServletRequest request) throws UniqloException {
        UsernamePasswordToken token = new UsernamePasswordToken(userName, password);
        Subject subject = SecurityUtils.getSubject();

        try {
            subject.login(token);
            return new APIResponse().success(null);
        } catch (UnknownAccountException e) {
            return new APIResponse().failure(400, "authentication failed", null);
        } catch (IncorrectCredentialsException e) {
            return new APIResponse().failure(400, "authentication failed", null);
        } catch (AuthenticationException e) {
            return new APIResponse().failure(400, "authentication failed", null);
        }
    }
}
