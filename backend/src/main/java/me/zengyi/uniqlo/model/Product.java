package me.zengyi.uniqlo.model;

import lombok.Data;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;

@Entity
@Table(name = "product")
@Data
public class Product implements Serializable {

    private static final long serialVersionUID = -1991280926836983949L;

    @Id
    private String id;

    @ManyToOne
    @JoinColumn(name = "kind_id")
    private Kind kind;

    private String productId;

    private Date insertedAt;

    private Date updatedAt;

    private String name;

    private String shortDescription;

    private String longDescription;

    private String careInstruction;

    private String composition;

    private String designDetail;

    private String freeInformation;

    private String sizeChartUrl;

    private String sizeInformation;

    private Long unisexFlag;

    private String washingInformation;
}
