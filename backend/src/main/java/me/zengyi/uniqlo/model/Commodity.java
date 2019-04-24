package me.zengyi.uniqlo.model;

import lombok.Data;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;

@Entity
@Table(name = "commodity")
@Data
public class Commodity implements Serializable {

    private static final long serialVersionUID = 1631542516809062979L;

    @Id
    private Long id;

    @ManyToOne
    @JoinColumn(name = "product_id")
    private Product product;

    @ManyToOne
    @JoinColumn(name = "color_code_id")
    private Color color;

    @ManyToOne
    @JoinColumn(name = "size_code_id")
    private Size size;

    @ManyToOne
    @JoinColumn(name = "pld_code_id")
    private Pld pld;

    @ManyToOne
    @JoinTable(name = "commodity_flag")
    private Flag flag;

    private String commodityId;

    private Date insertedAt;

    private String communicationCode;

    private Integer stockQuantity;

    private Boolean isSale;

    private Double price;

    private String priceCurrency;

    private Boolean isPromo;
}
