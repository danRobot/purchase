package com.ciclo4.purchase.reposotory;

import java.util.List;
import java.util.Optional;

import com.ciclo4.purchase.model.User;
import com.ciclo4.purchase.reposotory.CRUD.UserCRUDRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Repository;

@Repository
public class UserRepository {
    private static final String COLLECTION = "users";
    @Autowired
    private UserCRUDRepository repository;
    @Autowired
    private MongoTemplate mongoTemplate;
    /**
     * Operaciones GET
     */
    public List<User> listAll() {
        return repository.findAll();
    }
    public Optional<User> getUser(String email) {
        return repository.getUserByEmail(email);
    }
    public Optional<User> getUserId(String idf) {
        return repository.getUserByidentification(idf);
    }
    public User checkUser(String email, String password) {
        Optional<User> optional=repository.checkUser(email, password);
        if(optional.isEmpty()){
            return new User();
        }else{
            return optional.get();
        }
    }
    private long checkExistence(String key,String property) {
        Query query = new Query();
        query.addCriteria(Criteria.where(key).is(property));
        return mongoTemplate.count(query, COLLECTION);
    }
    /**
     * Operacion POST
     * @param user
     * @return
     */
    public Optional<User> postUser(User user){
        Optional<User> u=null;
        String email= user.getEmail();
        u=repository.getUserByEmail(email);
        if(u.isEmpty()){
            List<User> all=repository.findAll();
            int maxId=0;
            for (User user2 : all) {
                if(user2.getId()>maxId){
                    maxId=user2.getId();
                }
            }
            user.setId(maxId+1);
            return Optional.of(repository.insert(user));
        }else{
            return Optional.empty();
        }
    }
    /**
     * Operacion PUT
     * @param user
     * @return
     */
    public boolean putUser(User user) {
        String id=user.getIdentification();
        long users=checkExistence("identification", id);
        if (users>0) {
            Integer newId=repository.getUserByidentification(id).get().getId();
            user.setId(newId);
            repository.save(user);
            user=null;
            return true;
        } else {
            return false;
        }
    }
    /**
     * Operacion delete
     * @param user
     * @return
     */
    public void deleteUser(Integer id) {
        repository.deleteById(id);

    }
    public void deleteUsers(List<Integer> ids) {
        repository.deleteAllById(ids);
    }
    /**
     * Limpia colección de Usuarios
     */
    public void deleteAll(){
        repository.deleteAll();;
    }
    
}
