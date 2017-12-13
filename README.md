# ATQC
**_Preconditions_**
* vagrant should be installed `sudo apt-get install vagrant`
* virtualbox should be installed (5.1 version is preferably )
* `pip install -r req.txt`

#### _Vagrant_
vagrant **VM**, specified with IP **192.168.33.10** and name **monty_python**

**_How to use_**

* for runing `vagrant run`
* if u what to stop `vagrant halt`
* how to destroy `vagrant destroy`
* hot to ssh: `ssh vagrant@192.168.33.10` password: `vagrant`

----------------------------
### day_1

* The functions into `core.fibonaccie` module calculate and return positional fibo number.

  * `fibonacci_recursive` calculate `n` recursive, where n is position of fibo element
  * `fibonacci_math` - this one is pretty easy to implement and very, very fast to compute
  * `fibonacci_yield` - return the iterator, with help of that and `next()` function u can
     iterate it

  for printing the desired count of fibonacci numbers, `how_many_fibo_do_u_want` function into `main.py` module, has been implemented just input value, how many fibo numbers u want to get

* The function `find_pairs` into `numbers_pairs.py` modules get like an argument any collections ( list or tuple )
  modules get like an argument any collections ( list or tuple ) the second argument is the desired amount.

* The function `make_permutation_uniq` remove non uniq pairs.
----------------------------
### day_2

#### _Unit test_

* For unit test running `pytest -s -h tests`
----------------------------
### day_3
#### _Structuring project_

```
├── app_tests
├── cores
│   ├── fibonacci.py
│   └── numbers_pairs.py
├── tests
│   ├── test_fibo.py
│   └── test_permutation.py
├── main.py
├── README.mb
└── utils.py
```

* U should run `main.py` with help of key an now like `-f` and `-n`
  * `-f` or `--fib` if u wanna run fibbo func for example `python main.py --fib 5` u get something like this:
    ` args: (5,) kwargs: {} [0, 1, 1, 2, 3]`
  * `-n` or `--num` if u wanna get a pairs
  * `--help` can get u more information
----------------------------
### day_4
