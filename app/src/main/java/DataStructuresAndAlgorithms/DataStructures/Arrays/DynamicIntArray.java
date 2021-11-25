
package DataStructuresAndAlgorithms.DataStructures.Arrays;

import java.util.*;

interface IArray {

    public int getSize();

    public int get(int index);

    public void set(int index, int val);

    public void add(int elem);

    public void removeAt(int rm_index);

    public boolean remove(int elem);

    public boolean isEmpty();

}

/**
 * DynamicArrays : Integer Array
 */
public class DynamicIntArray implements IArray {

    // Actual DynamicArray size
    private int capacity = 0;

    // length user thinks DynamicArray is
    private int len = 0;

    private int[] arr;

    // Initialize default capacity of 16 in the case where capacity is not defined
    public DynamicIntArray() {
        this(16);
    }

    public DynamicIntArray(int capacity) {
        if (capacity < 0)
            throw new IllegalArgumentException("Illegal Capacity: " + capacity);
        this.capacity = capacity;
        arr = new int[capacity];
    }

    // Allows initializing the class using a predefined array
    public DynamicIntArray(int[] start_arr) {
        if (start_arr == null)
            throw new IllegalArgumentException("DynamicArray cannot be null");
        arr = Arrays.copyOf(start_arr, start_arr.length);
        capacity = len = start_arr.length;
    }

    public int getSize() {
        return len;
    }

    // For test purposes, ideally not public data
    public int getCapacity() {
        return this.capacity;
    }

    public boolean isEmpty() {
        return len == 0;
    }

    public int get(int index) {
        return arr[index];
    }

    public void set(int index, int elem) {
        arr[index] = elem;
    }

    public void add(int elem) {
        if (len + 1 >= capacity) {
            if (capacity == 0)
                capacity = 1;
            else
                capacity *= 2; // double the size
            arr = Arrays.copyOf(arr, capacity); // pads with extra 0/null elements
        }
        arr[len++] = elem;
    }

    // Removes the element at the specified index in this list.
    public void removeAt(int rm_index) {
        System.arraycopy(arr, rm_index + 1, arr, rm_index, len - rm_index - 1);
        --len;
        --capacity;
    }

    public boolean remove(int elem) {
        for (int i = 0; i < len; i++) {
            if (arr[i] == elem) {
                removeAt(i);
                return true;
            }
        }
        return false;
    }

    @Override
    public String toString() {
        if (len == 0)
            return "[]";
        else {
            StringBuilder sb = new StringBuilder(len).append("[");
            for (int i = 0; i < len - 1; i++)
                sb.append(arr[i] + ", ");
            return sb.append(arr[len - 1] + "]").toString();
        }
    }
}