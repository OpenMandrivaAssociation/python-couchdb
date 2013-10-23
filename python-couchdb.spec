%define srcname CouchDB
Name:           python-couchdb
Version:        0.9
Release:        1
Summary:        A Python library for working with CouchDB

Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/couchdb-python/
Source0:        http://pypi.python.org/packages/source/C/CouchDB/CouchDB-%{version}.tar.gz
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
python setup.py install --skip-build --root %{buildroot}

# calm rpmlint down
find  %{buildroot}/%{py_puresitedir}/couchdb -name \*.py -print0 | xargs --null chmod 0644


%clean

%files
%defattr(-,root,root,-)
%doc ChangeLog.txt COPYING README.txt 
%doc doc/
%{_bindir}/couchdb-dump
%{_bindir}/couchdb-load
%{_bindir}/couchdb-replicate
%{_bindir}/couchpy
%{py_puresitedir}/CouchDB-%{version}-py%{py_ver}.egg-info
%{py_puresitedir}/couchdb


%changelog
* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 0.8-2mdv2011.0
+ Revision: 590613
- rebuild for python 2.7

* Tue Aug 17 2010 Michael Scherer <misc@mandriva.org> 0.8-1mdv2011.0
+ Revision: 570880
- remove patch 1, just here to prevent some rpmlint warning
- update to 0.8
- merge -devel in main package, as this doesn't warrant a separate rpm

* Sun Apr 18 2010 Frederik Himpe <fhimpe@mandriva.org> 0.7-2mdv2010.1
+ Revision: 536260
- Version 0.7 no longer requires python-httplib2

* Fri Apr 16 2010 Frederik Himpe <fhimpe@mandriva.org> 0.7-1mdv2010.1
+ Revision: 535659
- update to new version 0.7

* Sat Feb 13 2010 Frederik Himpe <fhimpe@mandriva.org> 0.6.1-2mdv2010.1
+ Revision: 505607
- Does not require couchdb

* Fri Feb 12 2010 Frederik Himpe <fhimpe@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 505157
- Use %%py_requires macro
- First Mandriva package based on Fedora's
- create python-couchdb


