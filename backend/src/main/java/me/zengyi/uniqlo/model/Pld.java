package me.zengyi.uniqlo.model;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.io.Serializable;

@Entity
@Table(name = "pld")
@Data
public class Pld implements Serializable {

    private static final long serialVersionUID = 738114549210447700L;

    @Id
    private String code;

    private String displayCode;

    private String name;

}
