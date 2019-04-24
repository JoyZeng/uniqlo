package me.zengyi.uniqlo.service;

import me.zengyi.uniqlo.model.Kind;
import me.zengyi.uniqlo.repository.KindRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.List;

@Service
@Transactional
public class KindService {
    @Autowired
    private KindRepository kindRepository;

    public List<Kind> getKinds() {
        return kindRepository.findAll();
    }
}
