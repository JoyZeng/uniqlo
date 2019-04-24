package me.zengyi.uniqlo.repository;

import me.zengyi.uniqlo.model.Commodity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CommodityRepository extends JpaRepository<Commodity, Long> {

}
