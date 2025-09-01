package main

import (
	"fmt"
)

type LinkedList struct {
	value int
	key string

	Prev *LinkedList
	Next *LinkedList
}


type LRUCache struct {
	maxSize int
	currSize int

	cache 	map[string]*LinkedList
	head	*LinkedList
	tail 	*LinkedList
}

func NewLRUCache(size int) *LRUCache{
	return &LRUCache{maxSize: size, cache: make(map[string]*LinkedList, 0)}
}


// Time -> 0(1) Space -> 0(1)
func (lru *LRUCache) InsertKeyValuePair(key string, value int) {
	if pointer, exists := lru.cache[key]; exists {
		pointer.value = value
		lru.NewRecentlyUsed(pointer)
		return
	}
	if lru.currSize == lru.maxSize {lru.RemoveLRU(lru.head.key)}
	pointer := &LinkedList{value: value, key: key}
	lru.cache[key] = pointer
	lru.currSize = min(lru.currSize+1, lru.maxSize)
	if lru.head == nil {
		lru.head = pointer
		lru.tail = pointer
		return
	}
	pointer.Prev = lru.tail
	lru.tail.Next = pointer
	lru.tail = pointer
}


// Time -> 0(1) Space -> 0(1)
func (lru *LRUCache) GetValueFromKey(key string) (int, bool) {
	if val, exists := lru.cache[key]; exists {
		lru.NewRecentlyUsed(val)
		return val.value, true
	}
	return -1, false
}


// Time -> 0(1) Space -> 0(1)
func (lru *LRUCache) GetMostRecentKey() (string, bool) {
	if lru.currSize == 0 {
		return "", false
	}
	return lru.tail.key, true
}


func (lru *LRUCache) RemoveLRU(key string) {
	if lru.head.Next == nil {
		lru.head = nil
	}else {
		lru.head = lru.head.Next
		lru.head.Prev = nil
	}
	delete(lru.cache, key)
}


func(lru *LRUCache) NewRecentlyUsed(pointer *LinkedList) {
	if pointer == lru.tail {return}
	if pointer == lru.head {
		lru.head = lru.head.Next
		lru.head.Prev = nil

	}else {
		pointer.Prev.Next = pointer.Next
		pointer.Next.Prev = pointer.Prev
	}
	pointer.Prev = lru.tail
	lru.tail.Next = pointer
	lru.tail = pointer
	lru.tail.Next = nil
}

func min(x, y int) int {
	if x < y {return x}
	return y
}

func main() {
	lru := NewLRUCache(3)
	lru.InsertKeyValuePair("a", 1)
	lru.InsertKeyValuePair("b", 2)
	fmt.Println(lru.GetMostRecentKey())
	fmt.Println(lru.GetValueFromKey("a"))
	lru.InsertKeyValuePair("c", 3)
	fmt.Println(lru.GetMostRecentKey())
	lru.InsertKeyValuePair("d", 4)
	fmt.Println(lru.GetValueFromKey("b"))
}