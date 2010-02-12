%define srcname CouchDB
Name:           python-couchdb
Version:        0.6.1
Release:        %mkrel 1
Summary:        A Python library for working with CouchDB

Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/couchdb-python/
Source0:        http://pypi.python.org/packages/source/C/CouchDB/%{srcname}-%{version}.tar.gz
Patch0:         python-couchdb-shebang.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
BuildRequires:  python-setuptools python-devel
Requires:       couchdb
Requires:       python-httplib2
Requires:       python-simplejson

%package devel
Summary:        The  API reference files for CouchDB 
Group:          Development/Python
Requires:       %{name} = %{version}


%description
Providing a convenient high level interface for the CouchDB server.

%description devel
CouchDB python binding API reference documentation for use in development. 


%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1


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
%{_bindir}/couchdb-dump
%{_bindir}/couchdb-load
%{_bindir}/couchdb-replicate
%{_bindir}/couchpy
%{python_sitelib}/CouchDB-%{version}-py%{python_version}.egg-info
%{python_sitelib}/couchdb

%files devel
%defattr(-,root,root,-)
%doc doc/api doc/index.html
