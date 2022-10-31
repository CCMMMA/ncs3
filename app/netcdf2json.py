from netCDF4 import Dataset

def numpy_type_to_python_type(value):
    type_string = str(type(value))
    if "numpy." in type_string:
        if ".int32" in type_string:
            value = int(value)
        elif ".float32" in type_string:
            value = float(value)
    return value


#resource_url = "file:///mnt/instrdata/ccmmma/prometeo/data/opendap/wrf5/d01/history/2022/08/31/wrf5_d01_20220831Z1200.nc"

def netcdf2json(resource_url):

        data_set = Dataset(resource_url, "r")
        metadata = {
            "_id": resource_url,
            "mode": data_set.data_model,
            "dimensions": [],
            "variables": [],
            "attributes": {}
        }
        for dimension_name in data_set.dimensions:
            dimension = data_set.dimensions[dimension_name]
            dimesion_metadata = {
                "name": dimension_name,
                "size": dimension.size
            }
            if dimension.isunlimited():
                dimesion_metadata["unlimited"] = True

            metadata["dimensions"].append({"name": dimension_name, "size": int(dimension.size)})

        # print("Variables:")

        for variable_name in data_set.variables:
            variable = data_set.variables[variable_name]
            # print(variable_name, variable.shape, variable.dimensions)

            attributes_metadata = {}
            for attribute_name in variable.ncattrs():
                attributes_metadata[attribute_name] = numpy_type_to_python_type(variable.getncattr(attribute_name))

            variable_metadata = {
                "name": variable_name,
                "type": variable.datatype.name,
                "shape": list(variable.shape),
                "dimensions": list(variable.dimensions),
                "attributes": attributes_metadata
            }
            metadata["variables"].append(variable_metadata)

        for attribute_name in data_set.ncattrs():
            #       print(attribute_name,data_set.getncattr(attribute_name),type(data_set.getncattr(attribute_name)))
            metadata["attributes"][attribute_name] = numpy_type_to_python_type(data_set.getncattr(attribute_name))

        data_set.close()

        return metadata
