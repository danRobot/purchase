package com.ciclo4.purchase.reposotory;

/*import java.util.ArrayList;
import java.util.Date;*/
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
    public Optional<User> getUserbyId(Integer id) {
        return repository.findById(id);
    }
    public Optional<User> getUserId(String idf) {
        return repository.getUserByidentification(idf);
    }
    public List<User> getUserByMonth(String month){
        /*int nmo;
        List<User> allUsers=repository.findAll();
        List<User> byMonth=new ArrayList<User>();
        for (User user : allUsers) {
            nmo=user.month();
            System.out.println(user.getBirthtDay());
            System.out.println(nmo);
            if(nmo==month){
                byMonth.add(user);
            }
        }
        return byMonth;*/
        return repository.getUserByMonthBirthDay(month);
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
            if (user.getId()==null) {
                List<User> all=repository.findAll();
                int maxId=0;
                for (User user2 : all) {
                    if(user2.getId()>maxId){
                        maxId=user2.getId();
                    }
                }
                user.setId(maxId+1);
            }
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
    public User putUser(User user) {
        String id=user.getIdentification();
        long users=checkExistence("identification", id);
        if (users>0) {
            Integer newId=repository.getUserByidentification(id).get().getId();
            user.setId(newId);
            repository.save(user);
            //user=null;
            return user;
        } else {
            return new User();
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
