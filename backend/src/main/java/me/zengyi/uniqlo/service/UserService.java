package me.zengyi.uniqlo.service;

import lombok.extern.slf4j.Slf4j;
import me.zengyi.uniqlo.model.User;
import me.zengyi.uniqlo.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;


@Service
@Transactional
@Slf4j
public class UserService {

    @Autowired
    private UserRepository userRepository;

    public User getUserByUserName(String userName) {
        return userRepository.getUserByUserName(userName);
    }

}
