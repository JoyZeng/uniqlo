package me.zengyi.uniqlo.model;

import lombok.Data;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.io.Serializable;

@Entity
@Table(name = "color")
@Data
public class Color implements Serializable {

    private static final long serialVersionUID = -543414690714978344L;

    @Id
    private String code;

    private String displayCode;

    private String name;

}
