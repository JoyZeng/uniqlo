package me.zengyi.uniqlo.model;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.io.Serializable;

@Entity
@Table(name = "flag")
@Data
public class Flag implements Serializable {
    private static final long serialVersionUID = 484180562576149238L;

    @Id
    private Long id;

    private String code;

    private String name;
}
