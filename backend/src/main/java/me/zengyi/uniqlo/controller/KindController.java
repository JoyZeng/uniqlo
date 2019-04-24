package me.zengyi.uniqlo.controller;

import me.zengyi.uniqlo.common.APIResponse;
import me.zengyi.uniqlo.model.Kind;
import me.zengyi.uniqlo.service.KindService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class KindController {

    @Autowired
    private KindService kindService;

    @GetMapping("/kinds")
    public APIResponse getKinds() {
        return new APIResponse().success(kindService.getKinds());
    }
}
