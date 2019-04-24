package me.zengyi.uniqlo.model;

import lombok.Data;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;

@Entity
@Table(name = "review")
@Data
public class Review implements Serializable {

    private static final long serialVersionUID = -916227806695265251L;

    @Id
    private Long id;

    @JoinColumn(name = "product_id")
    private String productId;

    private Long ageRange;

    private String title;

    private String comment;

    private Date createdAt;

    private Integer genderCode;

    private String genderName;

    private String location;

    private String name;

    private Integer rate;

    private Boolean isRecommend;
}
