# Created by pyp2rpm-3.3.2
%global pypi_name pyrabbit2

Name:           python-%{pypi_name}
Version:        1.0.6
Release:        1%{?dist}
Summary:        A Pythonic interface to the RabbitMQ Management HTTP API

License:        MIT
URL:            https://github.com/deslum/pyrabbit2
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Fork module to communicate the RabbitMQ HTTP Management API main documentation
lives at 's no way to easily write programs against RabbitMQs management API
without resorting to some messy urllib boilerplate code involving HTTP Basic
authentication and parsing the JSON responses, etc. Pyrabbit abstracts this
away & provides an intuitive, easy way to work with the data that lives inside
of...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(requests)
%description -n python3-%{pypi_name}
Fork module to communicate the RabbitMQ HTTP Management API main documentation
lives at 's no way to easily write programs against RabbitMQs management API
without resorting to some messy urllib boilerplate code involving HTTP Basic
authentication and parsing the JSON responses, etc. Pyrabbit abstracts this
away & provides an intuitive, easy way to work with the data that lives inside
of...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Dec 07 2018 Matthias Runge <mrunge@redhat.com> - 1.0.6-1
- Initial package.
