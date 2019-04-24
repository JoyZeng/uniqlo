package me.zengyi.uniqlo.controller;

import lombok.extern.slf4j.Slf4j;
import me.zengyi.uniqlo.common.APIResponse;
import me.zengyi.uniqlo.exception.BadRequestException;
import me.zengyi.uniqlo.exception.UniqloException;
import me.zengyi.uniqlo.model.Review;
import me.zengyi.uniqlo.service.ReviewService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@Slf4j
@RestController
@RequestMapping("/review")
public class ReviewController {

    @Autowired
    private ReviewService reviewService;

    @GetMapping("")
    public APIResponse getReviews(@RequestParam("product_id") String productId) throws UniqloException {
        return new APIResponse()
                .success(reviewService.getReviewsByProductId(productId));
    }
}
