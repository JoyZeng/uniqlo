package me.zengyi.uniqlo.model;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.io.Serializable;

@Entity
@Table(name = "size")
@Data
public class Size implements Serializable {

    private static final long serialVersionUID = 5819949070819233055L;

    @Id
    private String code;

    private String displayCode;

    private String name;

}
