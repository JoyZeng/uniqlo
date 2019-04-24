package me.zengyi.uniqlo.controller;

import me.zengyi.uniqlo.common.APIResponse;
import me.zengyi.uniqlo.model.Flag;
import me.zengyi.uniqlo.service.FlagService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class FlagController {

    @Autowired
    private FlagService flagService;

    @GetMapping("/flags")
    public APIResponse getFlags() {
        return new APIResponse().success(flagService.getFlags());
    }
}
