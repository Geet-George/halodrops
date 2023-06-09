# {py:mod}`halodrops.sonde`

```{py:module} halodrops.sonde
```

```{autodoc2-docstring} halodrops.sonde
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Sonde <halodrops.sonde.Sonde>`
  - ```{autodoc2-docstring} halodrops.sonde.Sonde
    :summary:
    ```
* - {py:obj}`SondeData <halodrops.sonde.SondeData>`
  - ```{autodoc2-docstring} halodrops.sonde.SondeData
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_no_default <halodrops.sonde._no_default>`
  - ```{autodoc2-docstring} halodrops.sonde._no_default
    :summary:
    ```
````

### API

````{py:data} _no_default
:canonical: halodrops.sonde._no_default
:value: >
   None

```{autodoc2-docstring} halodrops.sonde._no_default
```

````

`````{py:class} Sonde
:canonical: halodrops.sonde.Sonde

```{autodoc2-docstring} halodrops.sonde.Sonde
```

````{py:attribute} sort_index
:canonical: halodrops.sonde.Sonde.sort_index
:type: numpy.datetime64
:value: >
   None

```{autodoc2-docstring} halodrops.sonde.Sonde.sort_index
```

````

````{py:attribute} serial_id
:canonical: halodrops.sonde.Sonde.serial_id
:type: str
:value: >
   None

```{autodoc2-docstring} halodrops.sonde.Sonde.serial_id
```

````

````{py:attribute} _
:canonical: halodrops.sonde.Sonde._
:type: dataclasses.KW_ONLY
:value: >
   None

```{autodoc2-docstring} halodrops.sonde.Sonde._
```

````

````{py:attribute} launch_time
:canonical: halodrops.sonde.Sonde.launch_time
:type: typing.Optional[typing.Any]
:value: >
   None

```{autodoc2-docstring} halodrops.sonde.Sonde.launch_time
```

````

````{py:method} __post_init__()
:canonical: halodrops.sonde.Sonde.__post_init__

```{autodoc2-docstring} halodrops.sonde.Sonde.__post_init__
```

````

````{py:method} add_spatial_coordinates_at_launch(launch_coordinates: typing.List) -> None
:canonical: halodrops.sonde.Sonde.add_spatial_coordinates_at_launch

```{autodoc2-docstring} halodrops.sonde.Sonde.add_spatial_coordinates_at_launch
```

````

````{py:method} add_launch_detect(launch_detect_bool: bool) -> None
:canonical: halodrops.sonde.Sonde.add_launch_detect

```{autodoc2-docstring} halodrops.sonde.Sonde.add_launch_detect
```

````

````{py:method} add_afile(path_to_afile: str) -> None
:canonical: halodrops.sonde.Sonde.add_afile

```{autodoc2-docstring} halodrops.sonde.Sonde.add_afile
```

````

````{py:method} add_postaspenfile(path_to_postaspenfile: str = None) -> None
:canonical: halodrops.sonde.Sonde.add_postaspenfile

```{autodoc2-docstring} halodrops.sonde.Sonde.add_postaspenfile
```

````

````{py:method} add_aspen_ds() -> None
:canonical: halodrops.sonde.Sonde.add_aspen_ds

```{autodoc2-docstring} halodrops.sonde.Sonde.add_aspen_ds
```

````

`````

`````{py:class} SondeData
:canonical: halodrops.sonde.SondeData

Bases: {py:obj}`halodrops.sonde.Sonde`

```{autodoc2-docstring} halodrops.sonde.SondeData
```

````{py:attribute} data
:canonical: halodrops.sonde.SondeData.data
:type: typing.Any
:value: >
   None

```{autodoc2-docstring} halodrops.sonde.SondeData.data
```

````

````{py:method} __post_init__()
:canonical: halodrops.sonde.SondeData.__post_init__

````

`````
