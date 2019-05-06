package me.zengyi.uniqlo.controller;

import lombok.extern.slf4j.Slf4j;
import me.zengyi.uniqlo.common.APIResponse;
import me.zengyi.uniqlo.exception.BadRequestException;
import me.zengyi.uniqlo.exception.UniqloException;
import me.zengyi.uniqlo.model.User;
import me.zengyi.uniqlo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;


@Slf4j
@RestController
@RequestMapping("/user")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/{userName}")
    public APIResponse getUserByUserName(@PathVariable("userName") String userName) throws UniqloException {
        User user = userService.getUserByUserName(userName);
        if (user != null) {
            return new APIResponse().success(user);
        } else {
            String message = "Product not found: " + userName;
            throw new BadRequestException(message);
        }
    }

}
