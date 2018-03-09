%{!?perl_vendorarch: %define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)}

Name:           perl-IO-Interface
Version:        1.09
Release:        1%{?dist}
Summary:        Perl extension for access to network card configuration information
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IO-Interface/
Source0:        http://www.planet-elektronik.de/CPAN//authors/id/L/LD/LDS/IO-Interface-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 0:5.005
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)

%description
IO::Interface adds methods to IO::Socket objects that allows them to be
used to retrieve and change information about the network interfaces on
your system. In addition to the object-oriented access methods, you can use
a function-oriented style.

%prep
%setup -q -n IO-Interface-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE META.json README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/IO*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 1.09-1
- Specfile autogenerated by cpanspec 1.78.
