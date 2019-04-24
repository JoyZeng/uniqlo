package me.zengyi.uniqlo.service;

import lombok.extern.slf4j.Slf4j;
import me.zengyi.uniqlo.model.Review;
import me.zengyi.uniqlo.repository.ReviewRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.List;

@Service
@Transactional
@Slf4j
public class ReviewService {

    @Autowired
    ReviewRepository reviewRepository;

    public List<Review> getReviewsByProductId(String productId) {
        return reviewRepository.getReviewsByProductId(productId);
    }
}
