package me.zengyi.uniqlo.repository;

import me.zengyi.uniqlo.model.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, String> {

}
