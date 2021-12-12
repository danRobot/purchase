package com.ciclo4.purchase;

import java.util.List;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;


/**
 * Clase para eliminar Documentos por Id
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class ListaIds {
    private List<Integer> lista;
}
