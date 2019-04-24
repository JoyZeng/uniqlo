package me.zengyi.uniqlo.service;

import lombok.extern.slf4j.Slf4j;
import me.zengyi.uniqlo.model.Product;
import me.zengyi.uniqlo.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;


@Service
@Transactional
@Slf4j
public class ProductService {

    @Autowired
    private ProductRepository productRepository;

    public Product getById(String id) {
        return productRepository.findById(id).orElse(null);
    }

}
