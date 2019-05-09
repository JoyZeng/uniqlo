package me.zengyi.uniqlo.model;

import lombok.Data;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;

@Entity
@Table(name = "role")
@Data
public class Role implements Serializable {

    private static final long serialVersionUID = 6448717044264993397L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private String description;

    private Date createdAt;

    private Date updatedAt;
}
