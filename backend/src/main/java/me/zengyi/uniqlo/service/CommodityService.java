package me.zengyi.uniqlo.service;

import lombok.extern.slf4j.Slf4j;
import me.zengyi.uniqlo.model.Commodity;
import me.zengyi.uniqlo.repository.CommodityRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;

@Service
@Transactional
@Slf4j
public class CommodityService {

    @Autowired
    private CommodityRepository commodityRepository;

    public Commodity getById(Long id) {
        return commodityRepository.findById(id).orElse(null);
    }

}
