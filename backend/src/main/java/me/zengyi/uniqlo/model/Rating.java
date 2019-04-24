package me.zengyi.uniqlo.model;

import lombok.Data;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;

@Entity
@Table(name = "rating")
@Data
public class Rating implements Serializable {

    private static final long serialVersionUID = 1071588117919809219L;

    @Id
    private Long id;

    @JoinColumn(name = "product_id")
    private String productId;

    private Date insertedAt;

    private Double average;

    private Double fit;

    private Integer oneCount;

    private Integer twoCount;

    private Integer threeCount;

    private Integer fourCount;

    private Integer fiveCount;
}
