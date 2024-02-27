#### Q1

```
Running dbt build, 
we build the whole project with a default value 'true' >> applying a limit 100 << to the staging models,
where the following lines appear

{% if var('is_test_run', default=true) %}
  limit 100
{% endif %}

and affecting the core ones, that are build on top of the staging models.

Therefore,
running dbt build --vars '{'is_test_run':'true'}'
has the same affect as dbt build
```

#### Q2

```
The code from the development branch we are requesting to merge to main
```

#### Q3

```
22998722
```

#### Q4

```
to be updated
```
####