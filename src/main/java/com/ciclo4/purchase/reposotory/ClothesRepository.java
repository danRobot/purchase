package com.ciclo4.purchase.reposotory;

import java.util.List;
import java.util.Optional;

import com.ciclo4.purchase.model.Clothes;
import com.ciclo4.purchase.reposotory.CRUD.ClothesCRUDRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Repository;

@Repository
public class ClothesRepository {
    private static final String COLLECTION = "clothes";
    @Autowired
    private ClothesCRUDRepository repository;
    @Autowired
    private MongoTemplate mongoTemplate;

    /**
     * Operaciones GET
     */

    public List<Clothes> listAll() {
        return repository.findAll();
    }
    public Optional<Clothes> getClothe(String reference) {
        return repository.getClothesByReference(reference);
    }
    private long checkExistence(String key,String property) {
        Query query = new Query();
        query.addCriteria(Criteria.where(key).is(property));
        return mongoTemplate.count(query, COLLECTION);
    }
    private Clothes getBykey(String key,String property) {
        Query query = new Query();
        query.addCriteria(Criteria.where(key).is(property));
        return mongoTemplate.findOne(query, Clothes.class);
    }
    public List<Clothes> getByPrice(String key,Integer price) {
        Query query = new Query();
        query.addCriteria(Criteria.where(key).is(price));
        return mongoTemplate.find(query, Clothes.class);
    }
    public List<Clothes> getByDescription(String description){
        return repository.getClothesByDescription(description);
    }
    /**
     * Operacion POST
     * @param clothes
     * @return
     */
    public Optional<Clothes> postClothes(Clothes clothes){
        Optional<Clothes> c=null;
        String reference= clothes.getReference();
        c=repository.getClothesByReference(reference);
        if(c.isEmpty()){
            return Optional.of(repository.insert(clothes));
        }else{
            return Optional.empty();
        }
    }

    /**
     * Operacion PUT
     * @param clothes
     * @return
     */
    public Clothes putClothes(Clothes clothes) {
        String id=clothes.getReference();
        long users=checkExistence("_id", id);
        if (users>0) {
            Clothes old=getBykey("_id",id);
            if(clothes.getCategory()==null){
                clothes.setCategory(old.getCategory());
            }
            if(clothes.getDescription()==null){
                clothes.setDescription(old.getDescription());
            }
            if(clothes.getPhotography()==null){
                clothes.setPhotography(old.getPhotography());
            }
            if(clothes.getPrice()==null){
                clothes.setPrice(old.getPrice());
            }
            if(clothes.getQuantity()==null){
                clothes.setQuantity(old.getQuantity());
            }
            if(clothes.getSize()==null){
                clothes.setSize(old.getSize());
            }
            return repository.save(clothes);
        } else {
            return new Clothes();
        }
    }
    /**
     * Operacion delete
     * @param user
     * @return
     */
    public void deleteClothes(String reference) {
        Optional<Clothes> op=repository.getClothesByReference(reference);
        if(op.isEmpty()){
            return;
        }else{
            repository.delete(op.get());
        }
    }
    /**
     * Limpia colección de Usuarios
     */
    public void deleteAll(){
        repository.deleteAll();;
    }
}
