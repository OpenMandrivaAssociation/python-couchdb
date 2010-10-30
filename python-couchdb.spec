%define srcname CouchDB
Name:           python-couchdb
Version:        0.8
Release:        %mkrel 2
Summary:        A Python library for working with CouchDB

Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/couchdb-python/
Source0:        http://pypi.python.org/packages/source/C/CouchDB/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
%py_requires -d
BuildRequires:  python-setuptools
Requires:       python-simplejson
# remove in 2013 once 2010.0 is not supported anymore
Obsoletes:       %{name}-devel < 0.8

%description
Providing a convenient high level interface for the CouchDB server.


%prep
%setup -q -n %{srcname}-%{version}

%build
python setup.py build


%install
rm -rf %{buildroot}
python setup.py install --skip-build --root %{buildroot}

# calm rpmlint down
find  %{buildroot}/%{python_sitelib}/couchdb -name \*.py -print0 | xargs --null chmod 0644


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog.txt COPYING README.txt 
%doc doc/
%{_bindir}/couchdb-dump
%{_bindir}/couchdb-load
%{_bindir}/couchdb-replicate
%{_bindir}/couchpy
%{python_sitelib}/CouchDB-%{version}-py%{python_version}.egg-info
%{python_sitelib}/couchdb
