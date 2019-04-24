package me.zengyi.uniqlo.model;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.io.Serializable;

@Entity
@Table(name = "kind")
@Data
public class Kind implements Serializable {

    private static final long serialVersionUID = 8106781898910004443L;

    @Id
    private Long id;

    private Long genderId;

    private Long classId;

    private Long categoryId;

    private Long subcategoryId;

    private String genderName;

    private String className;

    private String categoryName;

    private String subcategoryName;

}
