package me.zengyi.uniqlo.model;

import lombok.Data;

import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name = "image")
@Data
public class Image implements Serializable {

    private static final long serialVersionUID = 4613946405200023001L;

    @Id
    private Long id;

    @JoinColumn(name = "product_id")
    private String productId;

    private String colorDisplayCode;

    private String type;

    private String url;

}
