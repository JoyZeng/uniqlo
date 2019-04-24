package me.zengyi.uniqlo.controller;

import lombok.extern.slf4j.Slf4j;
import me.zengyi.uniqlo.common.APIResponse;
import me.zengyi.uniqlo.exception.BadRequestException;
import me.zengyi.uniqlo.exception.UniqloException;
import me.zengyi.uniqlo.model.Product;
import me.zengyi.uniqlo.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@Slf4j
@RestController
@RequestMapping("/product")
public class ProductController {

    @Autowired
    private ProductService productService;

    @GetMapping("/{id}")
    public APIResponse getProduct(@PathVariable("id") String id) throws UniqloException {
        Product product = productService.getById(id);
        if (product != null) {
            return new APIResponse().success(product);
        } else {
            String message = "Product not found: " + id;
            throw new BadRequestException(message);
        }
    }
}
