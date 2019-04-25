package me.zengyi.uniqlo.model;

import lombok.Data;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;

@Entity
@Table(name = "account")
@Data
public class User implements Serializable {

    private static final long serialVersionUID = 4153436681240061013L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String userName;

    private String nickname;

    private String password;

    private String email;

    private Date createdAt;

    private Date updatedAt;

    private Date lastLoginTime;

    private String status;
}
