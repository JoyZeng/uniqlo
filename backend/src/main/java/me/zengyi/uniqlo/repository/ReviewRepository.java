package me.zengyi.uniqlo.repository;

import me.zengyi.uniqlo.model.Review;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ReviewRepository extends JpaRepository<Review, Long> {
    List<Review> getReviewsByProductId(String productId);
}
