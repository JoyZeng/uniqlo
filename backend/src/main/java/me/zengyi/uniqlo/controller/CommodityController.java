package me.zengyi.uniqlo.controller;

import lombok.extern.slf4j.Slf4j;
import me.zengyi.uniqlo.common.APIResponse;
import me.zengyi.uniqlo.exception.BadRequestException;
import me.zengyi.uniqlo.exception.UniqloException;
import me.zengyi.uniqlo.model.Commodity;
import me.zengyi.uniqlo.service.CommodityService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@Slf4j
@RestController
@RequestMapping("/commodity")
public class CommodityController {

    @Autowired
    private CommodityService commodityService;

    @GetMapping("/{id}")
    public APIResponse getCommodity(@PathVariable("id") Long id) throws UniqloException {
        Commodity commodity = commodityService.getById(id);
        if (commodity != null) {
            return new APIResponse().success(commodity);
        } else {
            String message = "Commodity not found: " + id;
            throw new BadRequestException(message);
        }
    }
}
