package me.zengyi.uniqlo.service;

import me.zengyi.uniqlo.model.Flag;
import me.zengyi.uniqlo.repository.FlagRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.List;

@Service
@Transactional
public class FlagService {
    @Autowired
    private FlagRepository flagRepository;

    public List<Flag> getFlags() {
        return flagRepository.findAll();
    }
}
