package me.zengyi.uniqlo.repository;

import me.zengyi.uniqlo.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {

    User getUserByUserName(String userName);
}
